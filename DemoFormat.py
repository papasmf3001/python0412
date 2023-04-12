# DemoFormat.py 
url = "http://wwww.credu.com/?page=" + str(1)  
print(url)

for x in range(1,6):
    print(x,"*",x,"=",x*x)

print("---오른쪽정렬---")
for x in range(1,6):
    print(x,"*",x,"=", str(x*x).rjust(3))

print("---0으로 채우기---")
for x in range(1,6):
    print(x,"*",x,"=",str(x*x).zfill(5)) 


print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:,}".format(15000000))
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))
print("{0:.2f}".format(4/3))

#raw string notation:특수문자로 가공하지 않은 것 
f = open(r"c:\work\demo.txt", "wt", encoding="utf-8")
f.write("첫번째라인\n두번째라인\n세번째라인\n")
f.close() 
print( f.closed )

#파일을 읽기 
f = open(r"c:\work\demo.txt", "rt", encoding="utf-8")
result = f.read()
print("---readline()---")
f.seek(0)
print( f.readline(), end="" )
print( f.readline(), end="" )
f.seek(0)
lst  = f.readlines() 
print( lst )

f.close()
print( result )
