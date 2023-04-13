# DemoRE.py 
import re 
#search()함수와 match()함수의 차이 
result = re.search("[0-9]*th", "  35th")
print( result.group() )
print( result )

# result = re.match("[0-9]*th", "  35th")
# print( result.group() )
# print( result )

result = re.search("apple", "this is apple")
print(result.group())
result = re.search("\d{4}", "올해는 2023년입니다.")
print(result.group())
result = re.search("\d{5}", "우리 동네는 52300")
print(result.group())
