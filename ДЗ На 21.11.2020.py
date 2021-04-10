import random
answ=[]
for i in range(100):
    answ.append(random.randint(100, 250))
print(answ)
answ1=[]
for t in answ:
    if t not in answ1:
        answ1.append(t)
print(answ1)
b=0
for r in answ1:
    d1=r%10
    d2=r%100//10
    d3=r//100
    b+=d1
    b+=d2
    b+=d3
print(b)
print(len(answ1))
