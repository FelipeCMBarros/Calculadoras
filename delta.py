import math

a = float(input("Insira o valor da incógnita a: "))
b = float(input("Insira o valor da incógnita b: "))
c = float(input("Insira o valor da incógnita c: "))

delta = (b ** 2) -  4 * a * c

print("O valor de delta é:", delta)

if delta > 0:
  print("Existem duas raízes reais e iguais.")

elif delta < 0:
  print("Delta é negativo, assim não existem raízes.")

elif delta == 0:
  print("Delta é igual a 0, assim tendo duas raízes reais e iguais.")

else:
  print("Erro.")