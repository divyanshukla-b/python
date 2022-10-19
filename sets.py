
myset={1,2,3,4,5,6}
myset2=set({2,3,4,5,6,7})
myset2.add(8)
#myset2.discard(8)
#myset2.remove(8)
#print(myset2.pop())
#for x in myset2:
#    print(x)
#x = int(input("enter num"))
# '''if x in myset:
#     print("yes")
# else:
#     print("no")'''
print(myset.union(myset2))
print(myset.intersection(myset2))
print(myset.difference(myset2))
print(myset.symmetric_difference(myset2))

print(myset2.issubset(myset))
print(myset2.issuperset(myset))
print(myset2.isdisjoint(myset))
myset3=myset.copy()
print(myset)
myset.add(9)
print(myset3)
print(myset)
myset4=frozenset([89,78,67,56])

print((myset4))


