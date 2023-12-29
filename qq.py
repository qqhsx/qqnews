import requests

import os

import time

import logging

from concurrent.futures import ThreadPoolExecutor

import hashlib

import subprocess


logging.basicConfig(filename='news_crawler.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def sanitize_filename(filename):
    return "".join([c for c in filename if c.isalpha() or c.isdigit() or c in (' ','.','_')]).rstrip('.')

def remove_image_from_aa(file_path):
    if os.path.isfile(file_path):
        os.remove(file_path)
        logging.info(f"Removed image from 'aa' repository: {file_path}")
    else:
        logging.error(f"File not found in 'aa' repository: {file_path}")

def push_image_to_repo(file_path, output_dir, repo_name, repo_owner, branch='main', commit_message='Add new image'):
    access_token = os.getenv('IMAGE_REPO_TOKEN')  # 确保在Github Actions secrets中设置了IMAGE_REPO_TOKEN

    if access_token is None:
        raise ValueError("You must provide a Github access token in the environment variable 'IMAGE_REPO_TOKEN'")
    
    # 克隆目标仓库，如果已经克隆了就跳过

    if not os.path.isdir(repo_name):
        clone_cmd = [
            "git", "clone", 
            f"https://{access_token}@github.com/{repo_owner}/{repo_name}.git"
        ]
        subprocess.run(clone_cmd, check=True)
    
    # 将图片复制到仓库的相应目录

    repo_output_dir = os.path.join(repo_name, output_dir.strip('./'))  # strip leading './' from output_dir

    os.makedirs(repo_output_dir, exist_ok=True)
    subprocess.run(["cp", file_path, repo_output_dir], check=True)
    
    # 添加图片到git库中

    add_cmd = [
        "git", "-C", repo_name, "add", "."
    ]
    commit_cmd = [
        "git", "-C", repo_name, "commit", "-m", commit_message

    ]
    push_cmd = [
        "git", "-C", repo_name, "push", "origin", branch

    ]
    
    for cmd in [add_cmd, commit_cmd, push_cmd]:
        subprocess.run(cmd, check=True)
        
    # 清理图片，删除aa仓库中的图片

    remove_image_from_aa(file_path)

def download_image(url, output_dir, filename, repo_name='qqnews_image', repo_owner='qqhsx', retries=3):
    for i in range(retries):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)
                output_path = os.path.join(output_dir, filename)
                with open(output_path, "wb") as f:
                    f.write(response.content)
                
                # 在这里调用新函数把图片推送到'qqnews_image'仓库

                push_image_to_repo(output_path, output_dir, repo_name, repo_owner)

                return output_path

            else:
                logging.error(f"Failed to download image: {url}")
        except Exception as e:
            logging.error(f"Error occurred while downloading image: {url}\n{e}")
            if i < retries - 1:  # i is zero indexed

                logging.info(f"Retrying...({i+1}/{retries})")
                time.sleep(2)  # wait for 2 seconds before retrying

            else:
                logging.error(f"Failed to download image after {retries} attempts.")
    return None

def patch_fix_image_links(text, output_dir, title):
    img_pattern = r'!\[[^\]]*\]\([^)]*\)'
    img_links = re.findall(img_pattern, text)
    for img_link in img_links:
        fixed_img_link = img_link.replace('\n', '')
        text = text.replace(img_link, fixed_img_link)
        img_url = re.search(r'\((.*?)\)', fixed_img_link).group(1)
        filename = f"{hashlib.md5(img_url.encode()).hexdigest()}.jpg"
        download_image(img_url, output_dir, filename, retries=3)
        if filename:
            relative_path = f"./{title}/{filename}"
            text = text.replace(fixed_img_link, f"![{filename}]({relative_path})")
    text = re.sub(r'(!\[[^\]]*\]\([^)]*\))(\n{1,2})?', r'\1\n\n', text)
    text = re.sub(r'(!\[[^\]]*\]\([^)]*\))(.)', r'\1\n\n\2', text)
    return text

def process_article(title, url):
    try:
        tmphtml = requests.get(url).text
        tmpbs = bs(tmphtml, "html.parser")
        ss = str(tmpbs.select("div.LEFT div.content.clearfix")[0])
        ss = ss.replace("//inews.gtimg.com", "https://inews.gtimg.com").replace("</img>", "</img><br/>")
        ss = html2text.html2text(ss)
        if len(ss.split()) <= 3:
            logging.info(f"INVALID\n{title}\n{url}\n")
            return
        year = time.strftime('%Y')
        month = time.strftime('%m')
        day = time.strftime('%d')
        output_dir = os.path.join(sys.path[0], year, month, day)
        sanitized_title = sanitize_filename(title)
        img_dir = os.path.join(output_dir, sanitized_title)
        if not os.path.exists(img_dir):
            os.makedirs(img_dir)
        ss = patch_fix_image_links(ss, img_dir, sanitized_title)
        output_file = os.path.join(output_dir, f"{sanitized_title}.md")
        if os.path.exists(output_file):
            logging.info(f"EXIST\n{title}\n{url}\n")
            return
        with open(output_file, "w", encoding="utf-8") as x:
            x.write(ss)
        logging.info(f"SUCCESS\n{title}\n{url}\n")
    except Exception as e:
        logging.error(f"ERROR\n{title}\n{url}\n{e.args}\n======\n{traceback.format_exc()}\n")

def main():
    starttime = time.time()
    url1 = 'https://i.news.qq.com/trpc.qqnews_web.kv_srv.kv_srv_http_proxy/list?sub_srv_id=24hours&srv_id=pc&offset=0&limit=190&strategy=1&ext={"pool":["top","hot"],"is_filter":7,"check_type":true}'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}
    qq1 = requests.get(headers=headers, url=url1).json()
    datalist = []
    for i in qq1["data"]["list"]:
        tmptitle = i["title"]
        tmpurl = i["url"]
        if time.strftime("%Y%m%d") not in tmpurl:
            logging.info(f"EXPIRED\n{tmptitle}\n{tmpurl}\n")
            continue
        datalist.append(tuple([tmptitle, tmpurl]))
    with ThreadPoolExecutor(max_workers=5) as executor:
        for item in datalist:
            executor.submit(process_article, item[0], item[1])
    print(f"Total time taken: {time.time() - starttime} seconds")

if __name__ == '__main__':
    main()
