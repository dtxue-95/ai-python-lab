# # 先安装：!pip install beautifulsoup4
# from bs4 import BeautifulSoup
#
# # 用一段示例 HTML 演示解析（不依赖外网，可直接运行）
# html = """
# <html><body>
#   <h1>欢迎学习 Python</h1>
#   <p>第一段</p>
#   <p>第二段</p>
# </body></html>
# """
# soup = BeautifulSoup(html, "html.parser")
# title = soup.find("h1").text
# paragraphs = soup.find_all("p")
# print(f"网页标题: {title}")
# print(f"共 {len(paragraphs)} 个段落")

import os
import requests
from bs4 import BeautifulSoup

# 创建输出文件夹（如果不存在）
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# 1. 爬取数据
url = "https://quotes.toscrape.com/"
response = requests.get(url)
response.encoding = "utf-8"

if response.status_code != 200:
    print(f"请求失败，状态码：{response.status_code}")
    exit()

soup = BeautifulSoup(response.text, "html.parser")
quotes = soup.find_all("div", class_="quote")

# 存储爬取的内容（列表，每个元素是一个 (text, author) 元组）
data = []
for quote in quotes:
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text
    data.append((text, author))

# 2. 输出为 Markdown 文件（保存到 output 文件夹）
md_path = os.path.join(output_dir, "quotes.md")
with open(md_path, "w", encoding="utf-8") as md_file:
    md_file.write("# 名言摘录\n\n")
    for i, (text, author) in enumerate(data, 1):
        md_file.write(f"### {i}. {text}\n")
        md_file.write(f"*— {author}*\n\n")

# 3. 输出为 HTML 文件（保存到 output 文件夹）
html_content = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>名言摘录</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f9f9f9;
        }
        h1 {
            color: #2c3e50;
            text-align: center;
        }
        .quote-card {
            background: white;
            border-left: 5px solid #3498db;
            margin: 20px 0;
            padding: 15px 20px;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        .quote-text {
            font-size: 1.2em;
            font-style: italic;
            color: #2c3e50;
        }
        .quote-author {
            text-align: right;
            margin-top: 10px;
            font-weight: bold;
            color: #7f8c8d;
        }
    </style>
</head>
<body>
    <h1>📖 名言摘录</h1>
"""

for text, author in data:
    html_content += f"""
    <div class="quote-card">
        <div class="quote-text">“{text}”</div>
        <div class="quote-author">— {author}</div>
    </div>
    """

html_content += """
</body>
</html>
"""

html_path = os.path.join(output_dir, "quotes.html")
with open(html_path, "w", encoding="utf-8") as html_file:
    html_file.write(html_content)

print(f"✅ 已生成两个文件，保存在 '{output_dir}' 文件夹：")
print(f"   - {md_path}")
print(f"   - {html_path}")