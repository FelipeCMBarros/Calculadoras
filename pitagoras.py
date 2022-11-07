import math

conta = input("Você deseja calcular o cateto ou a hipotenusa? ")

if conta == "cateto":
  cat1 = float(input("Insira o valor do cateto conhecido: "))
  hip = float(input("insira o valor da hipotenusa: "))
  cat2 = (hip ** 2) - (cat1 ** 2)
  cat2resp = math.sqrt(cat2)

  print("O valor do segundo cateto é de:", cat2resp)

elif conta == "hipotenusa":
  cat1 = float(input("Insira o valor do primeiro cateto: "))
  cat2 = float(input("Insira o valor do segundo cateto: "))
  hip = (cat1 ** 2) + (cat2 ** 2)
  hipresp = math.sqrt(hip)
  print("O valor da hipotenusa é de: ", hipresp)

else:
  print("Por favor insira um tipo de operação válido.")