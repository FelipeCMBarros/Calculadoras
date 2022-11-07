import math

a = float(input("Insira o valor da incógnita a: "))
b = float(input("Insira o valor da incógnita b: "))
c = float(input("Insira o valor da incógnita c: "))

delta = (b ** 2) - 4 * a * c

if delta < 0:
  print("O valor do delta é de: ", delta)
  print("Delta teve valor negativo, assim sendo um número irreal.")

else:
  x1 = (-b + math.sqrt(delta)) / 2 * a
  x2 = (-b - math.sqrt(delta)) / 2 * a

  round(x1, 5)
  round(x2, 5)

  print("O valor do delta é de: ", delta)
  print("O valor de x¹ é de:", x1)
  print("O valor de x² é de:", x2)