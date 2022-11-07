import math

a = float(input("Insira o valor da incógnita a: "))
b = float(input("Insira o valor da incógnita b: "))
c = float(input("Insira o valor da incógnita c: "))

delta = (b ** 2) -  4 * a * c
x1 = (-b + math.sqrt(delta)) / 2 * a
x2 = (-b - math.sqrt(delta)) / 2 * a
x = -b / 2 * a
xv = -b / 2 * a
yv = - delta / 4 * a

round(x1, 5)
round(x2, 5)
round(x, 5)

print("O valor de delta é de:", delta)

if a > 0:
  print("A concavidade da parábola é para cima.")

elif a < 0:
  print("A concavidade da parábola é para baixo.")

else:
  print("Esta função não foi estudada ainda.")

if delta > 0:
  print("As coordenadas dos pontos de intersecção da parábola com o eixo x são: (", x1,", 0 ) e (", x2, ", 0)")

  print("As coordenadas do ponto de intersecção da parábola com o eixo y são: ( 0 ,", c,")")

  print("As coordenadas do vértice da parábola são: (", xv, ",", yv,")")

elif delta == 0:
  print("As coordenadas do ponto de intersecção da parábola com o eixo x são: (", x,", 0 )")

  print("As coordenadas do ponto de intersecção da parábola com o eixo y são: ( 0 ,", c,")")

  print("As coordenadas do vértice da parábola são: (", xv, ",", yv,")")

else:
  print("Delta é negativo, assim não tendo solução real.")