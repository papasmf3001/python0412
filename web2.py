# web2.py
#웹서버에 요청할 경우 사용
import requests
#크롤링 
from bs4 import BeautifulSoup

url = "https://www.daangn.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

f = open("c:\\work\\danngn.txt", "wt", encoding="utf-8")
posts = soup.find_all("div", attrs={"class":"card-desc"})
for post in posts:
    title = post.find("h2", attrs={"class":"card-title"}) 
    price = post.find("div", attrs={"class":"card-price"})
    print("{0} , {1}".format(title.text, price.text))
    f.write("{0} , {1}\n".format(title.text, price.text))

f.close() 

# <div class="card-desc">
#       <h2 class="card-title">나이키 옷 팔아요(새상품)</h2>
#       <div class="card-price ">
#         30,000원
#       </div>
#       <div class="card-region-name">
#         서울 구로구 구로제4동
#       </div>
