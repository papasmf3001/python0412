# class1.py 
#1)클래스 정의
class Person:
    #초기화 메서드
    def __init__(self):
        self.name = "default name"
    #일반 인스턴스 메서드
    def print(self):
        print("My name is {0}".format(self.name))

#2)인스턴스 생성
p1 = Person()
p2 = Person() 
p1.name = "전우치"

#3)메서드 호출
p1.print() 
p2.print() 

#런타임시에 변수 추가(동적형식)
Person.title = "new title"

print( p1.title )
print( p2.title )
print( Person.title )
