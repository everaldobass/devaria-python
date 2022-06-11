from src.capitulo02.poo.ContaBancaria import ContaBancaria
# Criando o Objeto conta
if __name__ == '__main__':
    conta1 = ContaBancaria ( "Everaldo", "Corrente", "0001", 123456, 100 )
    conta2 = ContaBancaria("Edson","Poupança", "0002", 654321, 200)

    print ( "\n************ Conta corrente *****************" )
    valordeposito = float(input("Deposite um valor R$:"))
    conta1.deposito(valordeposito)
    conta1.exibirDadosConta ()

    valorsaque = float(input("Valor do Saque R$: "))
    conta1.saque(valorsaque)
    conta1.exibirDadosConta()

    print("\n************ Conta poupança *****************")
    valordeposito = float ( input ( "Deposite um valor R$:" ) )
    conta2.deposito ( valordeposito )
    conta2.exibirDadosConta ()

    valorsaque = float ( input ( "Valor do Saque R$: " ) )
    conta2.saque ( valorsaque )
    conta2.exibirDadosConta ()
