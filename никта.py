#посчитать сумму всех четных цифр записанных в файл
with open('h.txt', 'r', encoding='UTF-8') as file:
    data = file.read()
print(data)
data = data.split(' ')
n=0
for i in data:
    if i.isdigit() and i%2==0:
        n+=1
print(n)
