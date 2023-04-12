# ifelse.py 
#다중라인 선택주석:ctrl + / 
# score = int(input("점수를 입력:"))

# if 90 <= score <= 100:
#     grade = "A"
# elif 80 <= score < 90:
#     grade = "B"
# elif 70 <= score < 80:
#     grade = "C"
# else:
#     grade = "D"

# print("등급은 ", grade)

value = 5 
while value > 0:
    print(value)
    value -= 1 

#순회가능한 형식(List, Dict, Tuple...)
lst = ["apple", 100, 3.14]
for item in lst:
    print(item, type(item))

fruit = {"apple":100, "kiwi":200}
for item in fruit.items():
    print(item)

print("---break---")
lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    if i > 5:
        break
    print("Item:{0}".format(i))

print("---continue---")
lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    if i % 2 == 0:
        continue 
    print("Item:{0}".format(i))

print("---range()---")
print( list(range(10)) )
print( list(range(2000,2024)) )
print( list(range(1,32)) )

print("---리스트 내장---")
lst = list(range(1,11))
print( [i**2 for i in lst if i > 5] )
tp = ("apple","orange","kiwi")
print( [ v.upper() for v in tp] )

print("---필터링---")
lst = [10,25,30]

def getBiggerThan20(i):
    return i > 20 
#내장함수
iterL = filter(getBiggerThan20, lst)
for item in iterL:
    print(item)

#람다함수
iterL = filter(lambda x:x>20, lst)
for item in iterL:
    print(item)
