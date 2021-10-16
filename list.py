mylist=["apple","banana","cheery","blueberry"]
print(mylist)
mylist.insert(2,"grapes")
mylist.remove("cheery")

print(mylist)
if "apple" in mylist:
    print("yes")
else:
    print("no")

#mylist.clear()

mylist.reverse()
print(mylist)

mylist2=[6,7,4,5,3,2,9]
mylist3 = sorted(mylist2)
print(mylist3)
print(mylist2)
mylist4=[9]*4
print(mylist4)
mylist5=mylist4+mylist2
print(mylist5)
print(mylist5[::4])

mylist6=list(mylist3)
print(mylist6)
b=[i*i for i in mylist6]
print(b)
