a = int(input("Quanto tu qué? porra! "))

bb = a // 100
b = a % 100

cc = b // 50
c = a % 50

dd = c // 10
d = a % 10

ee = d // 5
e = a % 5 

ff = e // 1
f = a % 1

if a > 600 or a < 10:
	print("Vá se foder!")

else:
	print("{} de 100 {} de 50 {} de 10 {} de 5 {} de 1".format(bb,cc,dd,ee,ff))