# DemoListTuple.py 
colors = ["red","blue","green"]
print( type(colors) )
print( len(colors) )
colors.append("yellow")
print( colors )
colors.insert(1, "white")
colors += "red"
print( colors )
print( colors.pop() )
print( colors.pop() )
colors.remove("red")
print( colors )

print("---set연습---")
a = {1,2,3,3}
b = {3,4,4,5}
print(a)
print(b)
print( a.union(b) )
print( a.intersection(b) )
print( a.difference(b) )

print("---tuple---")
tp = (100,200,300)
print( type(tp) )
print( len(tp) )
print( "id: %s, name: %s" % ("kim","김유신") )

def times(a,b):
    return a+b, a*b 

#호출
print(times(3,4))

print("---형식변환---")
a = set((1,2,3))
print(a)
b = list(a)
b.append(4)
print(b)
c = tuple(b)
print(c)
