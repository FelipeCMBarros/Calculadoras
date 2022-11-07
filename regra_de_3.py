print("Considerando os seguintes parâmetros: ")

print("    a   =   c")
print("    -       -")
print("    b       d")

input = input("Insira a incógnita desconhecida: ")

if input == "a":
    b = float(input("Insira o valor de b: "))
    c = float(input("Insira o valor de c: "))
    d = float(input("Insira o valor de d: "))
    r1 = b * c
    r2 = r1 / d
    print("O valor desconhecido é de:", r2)


elif input == "b":
    a = float(input("Insira o valor de a: "))
    c = float(input("Insira o valor de c: "))
    d = float(input("Insira o valor de d: "))
    r1 = a * d
    r2 = r1 / c
    print("O valor desconhecido é de:", r2)

elif input == "c":
    a = float(input("Insira o valor de a: "))
    b = float(input("Insira o valor de b: "))
    d = float(input("Insira o valor de d: "))
    r1 = a * d
    r2 = r1 / b
    print("O valor desconhecido é de:", r2)

elif input == "d":
    a = float(input("Insira o valor de a: "))
    b = float(input("Insira o valor de b: "))
    c = float(input("Insira o valor de c: "))
    r1 = b * c
    r2 = r1 / a
    print("O valor desconhecido é de:", r2)


else:
    print("Input colocado não é válido.")