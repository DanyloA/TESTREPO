a = 'kdfhfghkth rtgkhthrghtkg jgkggrj ktgkjtjkgjhrtg hrtkh rtgurtjgrtgjrtjg privet privet'
a.lower()
a = a.split(' ')
answ = {}
print(a)
for i in a:
    if i not in answ.keys():
        answ[i] = a.count(i)
print(answ)


def compare(integer):
    stepen = 0
    for i in str(integer):
        stepen += int(i)
        print(stepen)
    if integer > len(str(integer)) ** stepen:
        print('Число больше!')
    if integer < len(str(integer)) ** stepen:
        print('Число меньше!')
    else:
        return None
compare(1)


def peresozdanie_print(tip_danyx):
    answer = ''
    if isinstance(tip_danyx, str):
        for i in tip_danyx:
            if i.isalpha():
                answer += i
        print(answer)
    else:
        print(tip_danyx)


peresozdanie_print('efergregrergergergedrgergdreg2131231233213')
