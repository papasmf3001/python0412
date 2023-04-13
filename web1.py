# web1.py 
from bs4 import BeautifulSoup

#연속으로 함수나 메서드를 호출: 메서드체인
page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read() 
#검색이 용이한 객체
soup = BeautifulSoup(page, "html.parser")
print( soup.prettify() )


