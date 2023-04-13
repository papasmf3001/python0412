# db1.py
import sqlite3

#연결객체 생성(일단 메모리에서 임시 사용)
#con = sqlite3.connect(":memory:")
con = sqlite3.connect("c:\\work\\sample2.db")

#커서 객체를 생성
cur = con.cursor() 
#데이터를 저장한 테이블 구조(스키마) 생성 
cur.execute("create table if not exists PhoneBook " + 
    "(id integer primary key autoincrement, name text, phoneNum text);")
#1건 입력
cur.execute("insert into PhoneBook (name, phoneNum) values ('홍길동','010');")
#파라메터입력 
name = "이순신"
phoneNumber = "010-222"
cur.execute("insert into PhoneBook (name, phoneNum) values (?,?);", 
    (name,phoneNumber))
#다중의 레코드(행)입력 
datalist = (("박문수","010-333"), ("전우치","010-123"))
cur.executemany("insert into PhoneBook (name, phoneNum) values (?,?);", 
    datalist)

#검색
cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)

#작업을 완료하고 종료(예를 들면 오토커밋)
con.commit() 