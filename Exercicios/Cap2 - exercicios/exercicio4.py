distancia = float(input("Qual e a distancia da sua viagem em km? "))
if(distancia<= 200):
    print("Sua passagem custara R$ {:.2f}".format(distancia*0.5))
else:
    print("Sua passagem custara R$ {:.2f}".format(distancia*0.45))