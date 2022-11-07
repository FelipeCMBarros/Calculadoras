import math

raio = float(input("Insira o valor dos raios: "))
pi = float(input("Insira qual será considerado o valor de PI para essa conta: "))
ang = float(input("Insira o valor do ângulo: "))

c = 2 * pi * raio
resp1 = ang * c
resp2 = resp1 / 360

print("O valor da circunferência (C) é de:", c,"cm")
print("O valor do arco é de:", resp2, "cm")