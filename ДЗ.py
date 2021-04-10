a=[]
b=1
while b<201:
    if b%2==0:
        a.append(str(b))
    b+=1
print(a)
k=1
c=""
b=a
i=1
a.remove('2')
for i in range(1,80,1):
    if int(b[i])%10==2:
        a.remove(b[i])
    a[i]=a[i].replace('0','')
a.remove(a[7])
a.remove(a[-1])
print(a)

'''for o in range(1,11):
    if "0" in a[o]:
        int(a[o]).remove(d)
        print(a[o])'''
