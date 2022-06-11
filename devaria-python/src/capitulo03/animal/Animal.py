# Herança
class Animal:
    def __int__(self, nome:object, tamanho:object):
        self.nome = nome
        self.tamanho = tamanho

    def respirar(self):
        print(f"O Animal {self.nome} está respirando. O tamanho dele é {self.tamanho}")