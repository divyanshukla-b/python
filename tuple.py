mytuple=("sankalp",21,"kanpur")
print(len(mytuple))
print(mytuple.index("sankalp"))
print(mytuple.count("sankalp"))
mylist=list(mytuple)
print(type(mylist))
name,age,city=mytuple
print(name ,age,city)
mytuple2=(1,2,3,4)
i1,*i2=mytuple2
print(i1,i2)
print(type(i2))
