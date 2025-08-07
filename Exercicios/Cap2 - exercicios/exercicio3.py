sexo = input("Qual o seu sexo? (M = masculino, F = feminino): ")
while(sexo != "M" and sexo != "F"):
    sexo = input("Qual o seu sexo? (M = masculino, F = feminino):")
if(sexo == "M"):
    print("Você é um homem")
elif(sexo == "F"):
    print("Você é uma mulher")