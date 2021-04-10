file = open('Bukvy.txt','r')
r=file.read()
file.close()
file = open('Bukvy.txt','w')
for a in r:
	if a.isdigit():
		file.write(' ')
	else:
		file.write(a)
file.close()