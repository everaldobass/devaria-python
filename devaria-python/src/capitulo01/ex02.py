# Operadores lógicos
valido = False
print(not valido) # Resultado: True
print(not True) # Resultado : False

# Operador binário and - Checa a primeira condição se ela
# for False, nem avalia a segunda, só será True se ambas
# forem True.
def SecondOperand():
    print("Avaliando segundo operador.")
    return True

a = False and SecondOperand()
print(a)
b = True and SecondOperand()
print(b)