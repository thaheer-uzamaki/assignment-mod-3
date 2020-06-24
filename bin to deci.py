b=list(input("binary number: "))
v= 0
for i in range(len(b)):
	d=b.pop()
	if d== '1':
		v=v+pow(2, i)
print("decimal number:", v)