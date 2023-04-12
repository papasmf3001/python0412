# DemoDict.py 
device = {"아이폰":5, "아이패드":10, "윈도우":20}
print( device )
print( len(device) )
device["갤럭시"] = 15 
print( device["아이폰"] )
del device["윈도우"]
for item in device.items():
    print(item)

for k,v in device.items():
    print(k, v)

device["아이폰"] = 6 
print( device )

phone = {"kim":"1111", "lee":"2222", "park":"3333"}
#파이썬은 무조건 참조만 복사
p = phone 
print(phone)
print(p)
print( id(phone), id(p) )
print("moon" in phone)
print("moon" not in phone)
phone["kang"] = "1234"
print( phone )
print( p )
