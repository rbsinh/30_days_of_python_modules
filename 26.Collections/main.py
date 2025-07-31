# collections: counter,namedtupil, OrderDict, defeautdict, deque

from collections import Counter

from collections import namedtuple

from collections import OrderedDict

from collections import defaultdict

from collections import deque

a="aaabbbbcccccc"
my_counter=Counter(a)
print(my_counter.values())
print(my_counter.most_common(1)[0][0])
print(list(my_counter.elements()))

Point = namedtuple('Point','x,y')
pt = Point(1,-4)
print(pt.x,pt.y)

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 1
ordered_dict['c'] = 1
ordered_dict['d'] = 1
print(ordered_dict)

d = defaultdict(float)
d['a'] = 1
d['b'] = 2
print(d['c'])

d=deque()
d.append(1)
d.append(2)
d.appendleft(3)
print(d)
d.pop()
print(d)
d.popleft()
print(d)
d.extendleft([4,5,6])
print(d)
d.rotate(-2)
print(d)




