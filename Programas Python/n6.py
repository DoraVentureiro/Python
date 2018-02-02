
num = int(input("Escreva um número: "))
cnt = num // 100
dzn = num // 10 - cnt * 10
und = num // 1 - dzn * 10 - cnt * 100 

print(cnt, "Centena")
print(dzn, "Dezena")
print(und, """Unidade
""")

#===== Centenas =====#

if cnt == 1:
	print ("1 centena")
elif cnt > 1:
	print = ("{} centenas".format(cnt))
elif cnt == 1 and dzn != 0:
	print = ("centena,")
elif cnt > 1 and dzn != 0 :
	print = ("{}centenas,".format(cnt))

#===== Centenas =====#
#====================#
#====== Dezenas =====#

elif dzn == 1:
	print = ("dezena")
elif dzn > 1:
	print ("{} dezenas".format(dzn))
elif dzn == 1:
	print = ("dezena,")
elif dzn > 1:
	print = ("{} dezenas,".format(dzn))

#===== Dezenas ======#
#====================#
#===== Unidades =====#

elif und == 1:
	print = ("unidade")
elif und > 1:
	print = ("unidades".format(und))
elif und ==  1:
	print = ("e unidade")
elif und > 1:
	print = ("e unidades".format(und))

#===== Unidades =====#

else:
	print("O código tá errado burrão!")

#centena
#centenas
#centena,
#centenas,