import math

numero = float(input("Entre com um numero decimal: "))

print("A raiz de {} e igual a {}".format(numero, math.sqrt(numero)))
print("A funçao teto de {} e igual a {}".format(numero, math.ceil(numero)))
print("A funçao chao de {} e igual a {}".format(numero, math.floor(numero)))
print("A parte inteira de {} e igual a {}".format(numero,math.trunc(numero)))