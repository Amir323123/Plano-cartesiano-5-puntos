x1 = int(input("escriba la variable x1:"))
y1 = int(input('escriba la variable y1: '))
x2 = int(input('Escribe la variable x2: '))
y2 = int(input('Escribe la varible y2: '))
x3 =int(input("escriba la variable x3:"))
y3 = int(input('escriba la variable y3: '))
x4=int(input("escriba la variable x4:"))
y4 = int(input('escriba la variable y4: '))
x5 =int(input("escriba la variable x5:"))
y5 = int(input('escriba la variable y5: '))

d1=((x1-x2)+ (y1-y2))**2
d2=((x1-x3)+ (y1 -y3))**2
d3=((x1-x4)+ (y1 -y4))**2
d4=((x1-x5)+ (y1 -y5))**2
if d1<d2 and d1<d3 and d1<d4:
	print("el segundo punto esta mas cerca del primero")
elif d2<d1 and d2<d3 and d2<d4:
	print("el tercer punto esta mas cerca del primero")
elif d3<d1 and d3<d2 and d3<d4:
	print("el cuarto punto esta mas cerca del primero")
elif d4<d1 and d4<d2 and d4<d3:
	print("el quinto punto esta mas cerca del primero")
