from __future__ import absolute_import  # Permite importar outros scripts com funções

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
print("Transformação de temperaturas -> fahrenheit")

linhas()

print("Lembrete: decimais com ponto e não vírgula.")

input = (input("Escolha a operação que deseja executar: "))

linhas()

if input == "bhaskara":
    import bhaskara

elif input == "jurosC":
    import juros_composto

elif input == "jurosS":
    import juros_simples

elif input == "pitagoras":
    import pitagoras

elif input == "sincostan":
    import sin_cos_tan

elif input == "funcao afim":
    import funcao_afim

elif input == "funcao quad":
    import funcao_quadratica

elif input == "arco":
    import arco

elif input == "delta":
    import delta

elif input == "fahrenheit":
    import fahrenheit

elif input == "regra de 3":
    import regra_de_3

elif input == "testes":
    import testes

else:
    print("Operação colocada não é válida")