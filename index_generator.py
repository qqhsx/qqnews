import os
import re
from datetime import datetime

def generate_index_page(root_dir):
    index_file = os.path.join(root_dir, "index.html")

    articles = []

    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".md") and file != "index.md":
                # Extract the date from the directory structure
                dir_parts = subdir.split(os.sep)
                if len(dir_parts) >= 3:
                    year, month, day = dir_parts[-3:]
                    date_str = f"{year}-{month}-{day}"
                    try:
                        date = datetime.strptime(date_str, "%Y-%m-%d")
                    except ValueError:
                        continue  # 如果不能解析为日期，就跳过这个子目录
                else:
                    date = datetime.strptime("1970-01-01", "%Y-%m-%d")  # Use a default date if no date information is available

                title = os.path.splitext(file)[0]
                link = os.path.relpath(os.path.join(subdir, file), root_dir).replace("\\", "/")
                link = link.replace('.md', '.html')  # 新添加的行

                # Find the first image in the Markdown file
                with open(os.path.join(subdir, file), 'r', encoding='utf-8') as md_file:
                    md_content = md_file.read()
                    img_match = re.search(r'!\[.*?\]\((.*?)\)', md_content)
                    if img_match:
                        img_src = img_match.group(1)  # 直接使用从 Markdown 文件中提取的路径
                    else:
                        img_src = 'image/th.jpg'

                articles.append((date, title, link, img_src))

    # Sort the articles by date in descending order (most recent first)
    articles.sort(key=lambda x: x[0], reverse=True)

    with open(index_file, "w", encoding="utf-8") as f:
        f.write("<html>\n")
        f.write("<head>\n")
        f.write("<title>Article Index</title>\n")
        f.write("<style>\n")
        f.write("body {display: flex; flex-direction: column; align-items: center; background-color: #f5f5f5;}\n")
        f.write(".header {position: relative; text-align: center; margin: 20px 0;}\n")
        f.write(".header img {width: 100%; max-width: 680px; border-radius: 10px;}\n")
        f.write(".header .title {position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: white;}\n")
        f.write(".header .title h1 {font-size: 24px;}\n")
        f.write(".header .title h2 {font-size: 18px;}\n")
        f.write(".card {background-color: white; width: 680px; margin: 10px; padding: 10px; display: flex; box-sizing: border-box; transition: transform 0.3s; border-radius: 10px;}\n")
        f.write(".card:hover {transform: scale(1.05); box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);}\n")
        f.write(".card img {width: 220px; height: 145px; margin-right: 10px; object-fit: cover;}\n")
        f.write(".card .content {flex-grow: 1; margin-left: 20px;}\n")
        f.write(".card .content a {color: black; text-decoration: none; font-size: 18px;}\n")
        f.write(".card .content a:hover {text-decoration: underline;}\n")
        f.write(".card .image-container {width: 220px;}\n")
        f.write("</style>\n")
        f.write("</head>\n")
        f.write("<body>\n")

        f.write("<div class='header'>\n")
        f.write("<img src='image/prune.png' alt='Header Image'>\n")
        f.write("<div class='title'>\n")
        f.write("<h1>Main Title</h1>\n")
        f.write("<h2>Subtitle</h2>\n")
        f.write("</div>\n")
        f.write("</div>\n")

        for date, title, link, img_src in articles:
            f.write("<div class='card'>\n")
            f.write("<div class='image-container'>\n")
            f.write(f"<img src='{img_src}'>\n")
            f.write("</div>\n")
            f.write("<div class='content'>\n")
            f.write(f"<h2><a href='{link}'>{title}</a></h2>\n")
            f.write(f"<p>发表于 {date.strftime('%Y-%m-%d')}</p>\n")
            f.write("</div>\n")
            f.write("</div>\n")

        f.write("</body>\n")
        f.write("</html>\n")

if __name__ == '__main__':
    root_dir = os.path.dirname(os.path.abspath(__file__))  # This should be changed to the path of your aa repository
    generate_index_page(root_dir)
