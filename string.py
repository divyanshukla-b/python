mystring='sankalp chaturvedi'

print(mystring.strip())
print(mystring.upper())
print(mystring.startswith("s"))
print(mystring.endswith(" "))
print(mystring.find("a"))
print(mystring.count("a"))

print(mystring.replace("chaturvedi","sir"))
mystring2=mystring.split()
print(type(mystring2))
print(mystring2)
print(' '.join(mystring2))
var='is'
#sentence="he %s"%var
#print(sentence)
'''sentence="he {}".format(var)
print(sentence)'''
var2="bad guy"
sentence=f"he {var} {var2}"
print(sentence)


