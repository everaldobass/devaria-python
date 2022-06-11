# Operadores e Métodos

def somar(numero1, numero2):
    print(f"Soma de {numero1} + {numero2}")
    return numero1 + numero2

def subtrair(numero1, numero2):
    print(f"Subtração de {numero1} - {numero2}")
    return numero1 - numero2

def dividir(numero1, numero2):
    print(f"Divisão de {numero1} / {numero2}")
    return numero1 / numero2

def multiplicar(numero1, numero2):
    print(f"Multiplicação de {numero1} * {numero2}")
    return numero1 * numero2


n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

operador = input("Qual a operação matemática deseja fazer?(+, -, /, *): ")

resuldado = 0

if operador == "+":
    resultado = somar(n1, n2)
elif operador == "-":
    resuldado = subtrair(n1, n2)
elif operador == "/":
    resuldado = dividir(n1, n2)
elif operador == "*":
    resuldado = multiplicar(n1, n2)
else:
    print("Operador incorreto: ")

print(f"O valor da operação é: {resuldado}")

