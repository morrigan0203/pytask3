#2
l = [1,2,3,4,5,1,2,3,6,7,7,7,0]
res = {i for i in l if l.count(i) > 1}
print(res)

#3
MAX_LENGTH = 3
s = "Long string. Very long, a good long-long string! a long very Long putty length long short String Strong Long hello hello string"
print(s)
s2 = s.replace(",","").replace(".","").replace("!","").replace("?","")
l = s2.lower().split()
d = dict((x, l.count(x)) for x in set(l))
l2 = sorted(d.items(), key=lambda x:x[1], reverse=True)
l3 = l2[:MAX_LENGTH if len(l2) > MAX_LENGTH else len(l2)]
print(l3)

#4
CAPACITY_MAX = 14
d = {"котелок":5,"подложка":3,"куртка":2,"еда":4,"посуда":2,"консервы":1}
l = sorted(d.items(), key=lambda x:x[1], reverse=True)
backpack = []
weight = 0
for i in l:
    if weight + i[1] > CAPACITY_MAX:
        continue
    weight = weight + i[1]
    backpack.append(i)
print(weight, backpack)