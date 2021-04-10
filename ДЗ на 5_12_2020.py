data = [[13, 'scvasd'], 33, [15, 6, 18, '34523']]
h=0
for i in data:
        if isinstance(i, list):
            for g in i:
                if isinstance(g, int):
                    if g%2!=0 and len(str(g))==2:
                        h+=g
print(h)
