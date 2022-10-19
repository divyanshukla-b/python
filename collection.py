from collections import Counter
from collections import OrderedDict
from collections import namedtuple
from collections import defaultdict
from collections import deque




a = "aaabbbbbbcccc"
mycounter=Counter(a)
print(mycounter.keys())
print(mycounter.items())
print(mycounter.values())
print(mycounter.most_common(1)[0][0])
print(list(mycounter.elements()))


# point=namedtuple('point','x,y')
# pt=point(2,3)
# print(pt,pt.x,pt.y)

ordic=OrderedDict()
ordic['a']=1
ordic['b']=2
ordic['c']=3
ordic['d']=4
ordic['e']=5
print(ordic)

defdic=defaultdict(list)
defdic['a']=12
defdic['b']=34
print(defdic['v'])



dque=deque()
dque.append(2)
dque.append(9)
dque.appendleft(8)
print(dque.pop())
print(dque)
dque.extendleft([12,34,56])
print(dque)
dque.rotate(-2)
print(dque)


