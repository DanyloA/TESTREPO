import random
pari = {}
for i in range(1, 101):
    pari[i] = random.randint(100, 300)
print(pari)
print(len(pari))
smallest_value = pari[1]
biggest_value = 0
for i in pari:
    if pari[i] < smallest_value:
        smallest_value = pari[i]
print(smallest_value)
for i in pari:
    if pari[i] > biggest_value:
        biggest_value = pari[i]
print(biggest_value)
