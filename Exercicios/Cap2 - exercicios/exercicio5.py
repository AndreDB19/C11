numero = input("Escolha um numero entre 1000 e 9999:")
while(int(numero) < 1000 or int(numero) > 9999):
    numero = input("Escolha um numero entre 1000 e 9999:")
print("O numero da unidade e " + numero[3])
print("O numero da dezena e " + numero[2])
print("O numero da centena e "+ numero[1])
print("O numero do milhar e " + numero[0])