a=[31, 342, 120, 321, 10]
a.reverse()
ch=0
while ch<len(a):
    if '0' in a[ch]:
        a[ch].remove(0)
