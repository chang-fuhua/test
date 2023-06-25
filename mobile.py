import requests

url = "https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers"
response = requests.get(url)

if response.status_code == 200:
    html_content = response.text
    # 在这里解析网页内容和提取数据
else:
    print("请求失败")
