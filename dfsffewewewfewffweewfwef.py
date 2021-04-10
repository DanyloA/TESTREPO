import random
d=[]
while len(d)<101:
    d.append(random.randint(1,10))
print(d)
ch=0
while len(d)>ch:
    s=d.count(d[ch])
    if s>1:
        d.remove(d[ch])
    ch+=1
print(d)
