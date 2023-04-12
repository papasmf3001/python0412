# function1.py
#1)함수를 정의
def setValue(newValue):
    x = newValue 
    print("지역변수:", x)

#2)호출(중단점을 지정)
retValue = setValue(5)
print(retValue)

#함수정의
def swap(x,y):
    return y,x 

#호출
print( swap(3,4) )

#스코핑룰(LGB)
x = 1 
def func1(a):
    return x+a 

print(func1(1))

def func2(a):
    x = 5 
    return x+a 

print(func2(1))

#기본값(default value)
def times(a=10,b=20):
    return a*b 

print( times() )
print( times(5) )
print( times(5,6) )

#키워드인자방식(매개변수명을 기술)
def connectURI(server, port):
    strURI = "http://" + server + ":" + port 
    return strURI 

print( connectURI("ycampus.com", "80") )
print( connectURI(port="8080", server="ycampus.com") )

#가변인자를 처리
def union(*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result 

print( union("HAM","EGG") )
print( union("HAM","EGG","SPAM") )

#람다함수
g = lambda x,y:x*y 
print( g(3,4) )
print( g(5,6) )
print( (lambda x:x*x)(3) )
print( globals() )

