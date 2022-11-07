import math

cap = float(input("Insira a capital inicial: "))
juros = float(input("Insira a taxa de juros mensal (Em formato de 0.10 = 10%): "))
tempo = int(input("Insira a quantidade de tempo em meses: "))

montante = cap * ((1 + juros) ** tempo)
montante_final = round(montante, 2)

print("O montante final é de R$", montante_final)