import math

def linhas():
    print("-" * 50)


def mensagem1(msg):
    print("-" * 50)
    print("      ", msg)
    print("-" * 50)
    # 6 espaços + espaço automatico pycharm (7 total)


def mensagem2(msg):
    print("-" * 50)
    print("          ", msg)
    print("-" * 50)
    # 10 espaços + espaço automatico pycharm (11 total)


# Programa principal daqui em diante

mensagem1("Calculadoras pessoais: Felipe Barros")
mensagem2("Lista de operações e comandos")

print("Fórmula de Bhaskara -> bhaskara")
print("Juros composto -> jurosC")
print("Juros simples -> jurosS")
print("Teorema de pitágoras -> pitagoras")
print("Cálculo de seno, cosseno e tangente -> sincostan")
print("Função AFIM -> funcao afim")
print("Função quadrática/segundo grau -> funcao quad")
print("Cálculo de arco de circumferência -> arco")
print("Cálculo de delta -> delta")
print("Regra de 3 -> regra de 3")
print("Para finalizar o programa, digite alguma forma de 'pare.")

linhas()

print("Lembrete: decimais com ponto e não vírgula.")

def bhaskara():
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


def arco():
    raio = float(input("Insira o valor dos raios: "))
    pi = float(input("Insira qual será considerado o valor de PI para essa conta: "))
    ang = float(input("Insira o valor do ângulo: "))

    c = 2 * pi * raio
    resp1 = ang * c
    resp2 = resp1 / 360

    print("O valor da circunferência (C) é de:", c, "cm")
    print("O valor do arco é de:", resp2, "cm")

def delta():
    a = float(input("Insira o valor da incógnita a: "))
    b = float(input("Insira o valor da incógnita b: "))
    c = float(input("Insira o valor da incógnita c: "))

    delta = (b ** 2) - 4 * a * c

    print("O valor de delta é:", delta)

    if delta > 0:
        print("Existem duas raízes reais e iguais.")

    elif delta < 0:
        print("Delta é negativo, assim não existem raízes.")

    elif delta == 0:
        print("Delta é igual a 0, assim tendo duas raízes reais e iguais.")

    else:
        print("Erro.")

def funcao_afim():
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

def funcao_quad():
    a = float(input("Insira o valor da incógnita a: "))
    b = float(input("Insira o valor da incógnita b: "))
    c = float(input("Insira o valor da incógnita c: "))

    delta = (b ** 2) - 4 * a * c
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
        print("As coordenadas dos pontos de intersecção da parábola com o eixo x são: (", x1, ", 0 ) e (", x2, ", 0)")

        print("As coordenadas do ponto de intersecção da parábola com o eixo y são: ( 0 ,", c, ")")

        print("As coordenadas do vértice da parábola são: (", xv, ",", yv, ")")

    elif delta == 0:
        print("As coordenadas do ponto de intersecção da parábola com o eixo x são: (", x, ", 0 )")

        print("As coordenadas do ponto de intersecção da parábola com o eixo y são: ( 0 ,", c, ")")

        print("As coordenadas do vértice da parábola são: (", xv, ",", yv, ")")

    else:
        print("Delta é negativo, assim não tendo solução real.")

def juros_composto():
    cap = float(input("Insira a capital inicial: "))
    juros = float(input("Insira a taxa de juros mensal (Em formato de 0.10 = 10%): "))
    tempo = int(input("Insira a quantidade de tempo em meses: "))

    montante = cap * ((1 + juros) ** tempo)
    montante_final = round(montante, 2)

    print("O montante final é de R$", montante_final)

def juros_simples():
    cap = float(input("Insira a capital inicial: "))
    juros = float(input("Insira a taxa de juros mensal (Em formato de 0.10 = 10%): "))
    tempo = float(input("Insira a quantidade de tempo em meses: "))

    jurosmes = cap * juros
    montante = cap + jurosmes * tempo

    print("O juros mensal é de R$", jurosmes)
    print("O montande é de R$", montante)

def pitagoras():
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

def regra_de_3():
    print("Considerando os seguintes parâmetros: ")

    print("    a   =   c")
    print("    -       -")
    print("    b       d")

    comandoR3 = input("Insira a incógnita desconhecida: ")

    if comandoR3 == "a":
        b = float(input("Insira o valor de b: "))
        c = float(input("Insira o valor de c: "))
        d = float(input("Insira o valor de d: "))
        r1 = b * c
        r2 = r1 / d
        print("O valor desconhecido é de:", r2)


    elif comandoR3 == "b":
        a = float(input("Insira o valor de a: "))
        c = float(input("Insira o valor de c: "))
        d = float(input("Insira o valor de d: "))
        r1 = a * d
        r2 = r1 / c
        print("O valor desconhecido é de:", r2)

    elif comandoR3 == "c":
        a = float(input("Insira o valor de a: "))
        b = float(input("Insira o valor de b: "))
        d = float(input("Insira o valor de d: "))
        r1 = a * d
        r2 = r1 / b
        print("O valor desconhecido é de:", r2)

    elif comandoR3 == "d":
        a = float(input("Insira o valor de a: "))
        b = float(input("Insira o valor de b: "))
        c = float(input("Insira o valor de c: "))
        r1 = b * c
        r2 = r1 / a
        print("O valor desconhecido é de:", r2)


    else:
        print("Input colocado não é válido.")

while True: #while loop para repitir a pergunta da calculadora
    comando = (input("Escolha a operação que deseja executar: "))
    linhas()

    if comando == "bhaskara":
        bhaskara()
        linhas()

    elif comando == "jurosC":
        juros_composto()
        linhas()

    elif comando == "jurosS":
        juros_simples()
        linhas()

    elif comando == "pitagoras":
        pitagoras()
        linhas()

    elif comando == "funcao afim":
        funcao_afim()
        linhas()

    elif comando == "funcao quad":
        funcao_quad()
        linhas()

    elif comando == "arco":
        arco()
        linhas()

    elif comando == "delta":
        delta()
        linhas()

    elif comando == "regra de 3":
        regra_de_3()
        linhas()

    elif comando == "pare" or "para" or "parar" or "Pare" or "Para" or "Parar" or "stop" or "Stop":
        print("Programa finalizado com sucesso.")
        break #termina o while o loop, nesse caso o código

    else:
        print("Operação colocada não é válida, tente novamente.")