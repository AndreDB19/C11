numero = input("Escolha um numero: ")
comeco = input("Escolha o começo da tabuada: ")
fim = input("Escolha o fim da tabuada: ")

print(f"Tabuada do {numero} de {comeco} a {fim}:")
for i in range(int(comeco), int(fim)+1):

   soma =  int(numero)*int(i)
   print(soma)