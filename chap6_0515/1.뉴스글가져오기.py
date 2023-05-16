#crtl + shift + p / select interpreter / base 선택
#pip install beautifulsoup4
from bs4 import BeautifulSoup

import requests #http 요청 처리 library

headers = {
    "User-Agent": "Dongyang Mirae"
}
#뉴스
webpage = requests.get("https://n.news.naver.com/article/047/0002392320", headers=headers)

print(webpage)

soup = BeautifulSoup(webpage.content, "html.parser")

print(soup)

news = soup.select_one("#dic_area").get_text().strip()
print(news)