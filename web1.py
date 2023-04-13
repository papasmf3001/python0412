# web1.py 
from bs4 import BeautifulSoup

#연속으로 함수나 메서드를 호출: 메서드체인
page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read() 
#검색이 용이한 객체
soup = BeautifulSoup(page, "html.parser")
#print( soup.prettify() )
#<p>태그를 전체를 검색 
#print( soup.find_all("p") ) 
#첫번째<p>만 검색 
# print( soup.find("p") )
#조건(필터링): <p class="outer-text">
#print( soup.find_all("p", class_="outer-text") )
#attrs(속성들)
#print( soup.find_all("p", attrs={"class":"outer-text"}) )
#태그 내부에 문자열만 추출
for tag in soup.find_all("p"):
    title = tag.text.strip() 
    title = title.replace("\n", "")
    print(title)









