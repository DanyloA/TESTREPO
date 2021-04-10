#integer = int(input('www.com'))
#answ=0
#answ=answ+integer//100
#answ=answ+integer%10
#answ=answ+integer//10
#print(answ)
#km=int(input())
#b1=int(input())
#b2=int(input())
#if b1>b2:
#    print('fryfyuergfegrfgegfuerfygerfyerfygerfyuzааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааа я не могу пока пока пока')
#else:
#    print(km/b1 - km/b2)
#answ=0
#proverka=0
#for i in range(10,1000):
#    proverka=i
#   if
#  if str(proverka[0]) % 2==0:
#   print(answ)
#    answ+=1
#       proverka=0
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
#def dvestroki(stroka):
    #stroki=''
    #integers=''
    #for i in stroka:
      #  if i.isdigit():
     #       integers+=i
    #    if i.isalpha():
   #         stroki+=i
  #  answ=[integers,stroki]
 #   return answ
#print(dvestroki('duey6erfhrfejrfdedede6f67erf6'))
data = {}
for i in range(1, 101):
    data[i] = i ** 2
answ = {}
for i in range(1, 101):
    answ[data[i]] = i
print(answ)

