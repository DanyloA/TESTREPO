d = int(input('bbb'))
start = [d, []]
ch = d - 1
while ch >= 1:
    answer = [ch, start]
    start = answer
    ch -= 1
    print(answer)
