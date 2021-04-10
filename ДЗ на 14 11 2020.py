f=[]
j=1
h=0
while True:
    if j%2==1:
        if '7' in str(j) and '2' in str(j):
            f.append(j)
            h+=1
    if h==123:
        break
    j-=-1
print(f)
f.reverse()
print(f)
