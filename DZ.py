import random
mylist=['']
index=0
for i in range(0,1000):
    proverka=mylist[index]
    mylist.append(random.randint(100000, 999999))
    if proverka in mylist:
        while True:
            if proverka in mylist:
                mylist[index]=random.randint(10000, 999999)
            elif proverka not in mylist:
                break
    index+=1
print(mylist)
schasliviybilet=0
countparniyinteger=0
countneparniyinteger=0
for i in mylist:
    for a in str(i):
        if int(a)%2==0:
            countparniyinteger+=int(a)
        else:
            countneparniyinteger+=int(a)
        if countneparniyinteger==countparniyinteger:
           schasliviybilet+=1
       countneparniyinteger=0
        countparniyinteger=0
print(schasliviybilet)
