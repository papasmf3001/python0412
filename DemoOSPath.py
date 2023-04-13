# DemoOSPath.py 
from os.path import * 
from os import * 
from glob import * 

#print( dir() )
print( abspath("python.exe") )
print( basename("c:\\work\\python.exe") )
if exists("c:\\python310\\python.exe"):
    print("파일크기:{0}".format(getsize("c:\\python310\\python.exe")))
else:
    print("파일없음")

system("notepad.exe")

print("운영체제이름:{0}".format(name))

result = glob("c:\\work\\*.py")
print(result)



