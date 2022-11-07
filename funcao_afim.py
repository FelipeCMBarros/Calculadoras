import math

a = float(input("Insira o valor de a: "))
b = float(input("Insira o valor de b: "))

variavel = input("Deseja calcular o valor de y sabendo x, x sabendo y ou a raiz? ")

if variavel == "x":
    y = float(input("Insira o valor de y: "))
    resp1 = y - b
    resp2 = resp1 / a
    x = resp2

    print("O par ordenado é de ( ", x, ", ", y, ")")


elif variavel == "y":
    x = float(input("Insira o valor de x: "))
    y = a * x + b

    print("O par ordenado é de (", x, ",", y, ")")

elif variavel == "raiz":
    resp1 = b / (- a)
    print("A raiz da função é de ( ", resp1, ", 0 )")

else:
    print("Cálculo inserido é invalido")