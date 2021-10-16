mydict={"name":"sankalp","age":21,"city":"kanpur"}
#print(mydict["name"])
mydict.pop("age")
#del mydict["name"]
print(mydict)
if "email" in mydict:
    print("yes")
else:
    print("no")
try:
    print(mydict["email"])
except:
    print("error")
mydict["email"]="sankalp@gmail.com"
print(mydict)
try:
    print(mydict["email"])
except:
    print("error")
mydictcpy=mydict.copy()
print(mydict)
mydict["ph no"]=7754008033
print(mydict)
print(mydictcpy)
mydict2=dict(gender="male")
mydict.update(mydict2)
print(mydict)
for value,key in mydict.items():
    print(value,key)
mytuple=(1,2)
mydict2["vla"]=mytuple
print(mydict2)






