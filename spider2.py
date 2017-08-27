# coding:utf-8
import requests
from bs4 import BeautifulSoup

quesNumStr = str(input("请输入搜索关键字："))

url = 'https://www.zhihu.com/search?type=content&q=' + quesNumStr

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'
# your user-Agent here
}

data = requests.get(url, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')
liList = soup.select('li')
print(len(liList))
for li in liList:
    try:
        temp1 = li.select('a[class="js-title-link"]')
        if temp1:
            print('The title is :')
            print(temp1[0].get_text())
        temp2 = li.select('div[class="summary hidden-expanded"]')
        if temp2:
            print('The content is:')
            print(temp2[0].text)
    except:
        pass