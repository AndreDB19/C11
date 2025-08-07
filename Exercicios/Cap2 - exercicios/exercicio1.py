nome = input("Qual e o seu nome? ")
NomeMaiusculo = nome.upper()
print("Maiusculo: " + NomeMaiusculo)

NomeMinusculo = nome.lower()
print("Minusculo: " + NomeMinusculo)

NumeroLetras = len(nome.replace(" ", ""))
print("Numero de Letras: " + str(NumeroLetras))


NomeSeparado = nome.split()
NomeSeparado[-1]="do inatel"

NomeSubstituido = ""
for i in range(len(NomeSeparado)):
    NomeSubstituido = NomeSubstituido + NomeSeparado[i] + " "

print("Nome com 'do Inatel': " + NomeSubstituido)