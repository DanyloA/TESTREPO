t=input()
f=t if str(t[::-1])!=t and '7' in str(t) and int(t)%2==0 else None
print(f)
f=input()
g=True if '7' in f and f[0]=='b' else False
print(g)
