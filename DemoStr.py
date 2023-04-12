# DemoStr.py 
strA = "python is very powerful"
strB = "파이썬은 강력해"

print( len(strA) )
print( len(strB) )
print( strA.capitalize() )
print( strA.count("p") )
print( strA.startswith("py") )
print( strA.endswith("ful") )
print( "MBC2580".isalnum() )
print( "MBC:2580".isalnum() )
print( "2580".isdecimal() )

#데이터를 가공할 경우
u = "<<<  spam and ham  >>>"
result = u.strip("<> ")
print(u)
print(result)
result = result.replace("spam", "spam egg")
print(result)
lst = result.split() 
print(lst)
print( ":)".join(lst) )

