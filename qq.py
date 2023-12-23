import requests
import os
import time
import html2text
import sys
import traceback
from bs4 import BeautifulSoup as bs
import re
import logging
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(filename='news_crawler.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def patch_fix_image_links(text):
    # 正则表达式来匹配Markdown中的图片链接
    img_pattern = r'!\[[^\]]*\]\([^)]*\)'

    # 找到所有的图片链接
    img_links = re.findall(img_pattern, text)

    # 遍历图片链接并修复其中的换行符
    for img_link in img_links:
        fixed_img_link = img_link.replace('\n', '')
        text = text.replace(img_link, fixed_img_link)

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
        output_dir = f"{sys.path[0]}/{time.strftime('%Y-%m-%d')}"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        output_file = f"{output_dir}/{title}.md"
        if os.path.exists(output_file):
            logging.info(f"EXIST\n{title}\n{url}\n")
            return
        # 修复Markdown文件中的图像链接和换行符
        ss = patch_fix_image_links(ss)
        
        # 添加链接与文字分行显示的逻辑
        ss = re.sub(r'(!\[[^\]]*\]\([^)]*\))(\s+)(\S)', r'\1\n\3', ss)
        
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

    # 使用线程池处理文章下载和处理
    with ThreadPoolExecutor(max_workers=5) as executor:
        for item in datalist:
            executor.submit(process_article, item[0], item[1])

    print(f"总共耗时: {time.time() - starttime} 秒")

if __name__ == '__main__':
    main()
