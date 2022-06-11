#  Definição de uma Classe
class ContaBancaria:
    def __init__(self, titular: object, tipo: object, agencia: object, conta: object, saldo: object) -> object:
        self.titular = titular
        self.tipo = tipo
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def exibirDadosConta(self):
        print(f"Titular: {self.titular}")
        print(f"Tipo: {self.tipo}")
        print ( f"Agencia: {self.agencia}" )
        print ( f"Agencia: {self.conta}" )
        print(f"Saldo Conta R$: {self.saldo}")

    def saque(self, valor):
        if self.saldo >= valor:
            print(f"Realizando um saque no valor de R${valor}")
        else:
            print(f"Saldo insuficiente R${valor}")
        self.saldo -= valor

    def deposito(self, valor):
        self.saldo += valor
        print(f"Realizando um deposito de R${valor}")





