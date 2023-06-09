#부모 클래스 
class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(
            self.name, self.phoneNumber))
#자식 클래스 
class Student(Person):
    #상속을 받고 재정의(덮어쓰기)
    def __init__(self, name, phoneNumber, subject, studentID):
        #명시적으로 부모클래스 초기화 메서드 호출
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(
            self.name, self.phoneNumber))
        print("Info(StudentID:{0}, Subject: {1})".format(
            self.studentID, self.subject))
        
p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "빅데이터", "231234")
p.printInfo()
s.printInfo() 



