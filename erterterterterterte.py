import random
b=[]
for i in range(1,20):
    b.append(random.randint(1,7))
print(b)
v=0
m=[]
for p in b:
    h=b[v]
    v+=1
    m.clear()
    c=v+1
    m.append(b[c:h])
    b[v:h] =m,
print(b)
