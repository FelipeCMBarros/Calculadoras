import math

cap = float(input("Insira a capital inicial: "))
juros = float(input("Insira a taxa de juros mensal (Em formato de 0.10 = 10%): "))
tempo = float(input("Insira a quantidade de tempo em meses: "))

jurosmes = cap * juros
montante = cap + jurosmes * tempo

print("O juros mensal é de R$", jurosmes)
print("O montande é de R$", montante)