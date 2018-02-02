num = int(input("Escreva um número: "))
cnt = num // 100
dzn = num // 10 - cnt * 10
und = num // 1 - dzn * 10 - cnt * 100 

if cnt == 0 and dzn == 0 and und == 0:
	print("Nenhuma Centena, Dezena, Unidade.")
	
elif cnt == 1 and dzn == 0 and und == 0:
	print("1 Centena.")
	
elif cnt == 1 and dzn == 1 and und == 0:
	print("1 Centena e 1 Dezena.")
	
elif cnt == 1 and dzn == 1 and und == 1:
	print("1 Centena, 1 Dezena e 1 Unidade.")
	
elif cnt == 0 and dzn == 1 and und == 1:
	print("1 Dezena e 1 Unidade.")
	
elif cnt == 0 and dzn == 0 and und == 1:
	print("1 Unidade.")
	
elif cnt == 1 and dzn == 0 and und == 1:
	print("1 Centena e 1 Unidade.")
	
elif cnt == 0 and dzn == 1 and und == 0:
	print("1 Dezena")
	
elif 

#000
#100
#110
#111
#011
#001
#101
#010
#002
#022
#222
#220
#200
#202
#020