"""
Faça um programa para uma loja de tintas.

 O programa deverá pedir o tamanho em metros quadradados da área a ser pintada.
 Considere que a cobertura da tinta e de 1 litro para cada 3 metros quadrados
 e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
 
 Informe ao usuário a quantidade de latas de tinta
 a serem compradas e o preço total.
 """
mqd = int(input("Qual a área à ser pintada? "))
x = mqd/3
y = (int(x) + ((int(x) - x) != 0))
z = y/18
xx = (int(z) + ((int(z) - z) != 0))

if y <= 18:
	print("Você precisará de 1 lata de tinta! Lhe custará R$ 80,00.")

if y > 18:
	print("Você precisará de {} latas de tinta! Lhe custará R$ {},00.".format(xx, xx * 80))