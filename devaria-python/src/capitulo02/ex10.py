# Esver um programa que recebe alguns produtos como argumento
# Validar se esse produto estão na lista de itens disponiveis do mercado
# Caso esteja acisar o usuário quais produtos tem e quais não tem e
# por ultimo exibir a lista de produtos dispoinveis ordenadas por ordem alfabética

try:
    produtoDisponiveis = ["Uva", "Maça", "Abacaxi", "Laranja"]
    listaProdutos = []
    produto = None

    print ("Produtos disponiveis: ")
    produtoDisponiveis.sort()
    print(produtoDisponiveis)

    while True:
      produto = input("Digite a lista de produto que deseja: (Digite 0 para finalizar): ")

      if produto in produtoDisponiveis:
         listaProdutos.append(produto)
      else:
         print(f"O produto {produto} não está disponivel")

      if produto == '0':
        break

    print("Produtos disponiveis")
    print(produtoDisponiveis)

    print("Produtos comprados")
    print(listaProdutos)

except Exception as e:
    print(e)

