# db1.py
import sqlite3

#연결객체 생성(일단 메모리에서 임시 사용)
con = sqlite3.connect(":memory:")
#커서 객체를 생성
cur = con.cursor() 
#데이터를 저장한 테이블 구조(스키마) 생성 
cur.execute("create table if not exists PhoneBook " + 
    "(id integer primary key autoincrement, name text, phoneNum text);")
#1건 입력
cur.execute("insert into PhoneBook (name, phoneNum) values ('홍길동','010');")
#검색
cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)

