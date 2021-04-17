chislo = int(input())
kolychestvo_rasdelenyi_na_2 = 0
while True:
    if chislo % 2 == 0:
        kolychestvo_rasdelenyi_na_2 += 1
        chislo /= 2
    if chislo % 2 != 0:
        break
print(kolychestvo_rasdelenyi_na_2)
