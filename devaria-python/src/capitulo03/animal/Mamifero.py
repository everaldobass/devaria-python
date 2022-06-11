from src.capitulo03.Animal import Animal

class Mamifero ( Animal ):
    def __int__(self, nome: object, tamanho: object):
        super ().__int__ ( nome, tamanho )

    def Alimentar(self):
        print ( f"O animal{self.nome} está alimentando. O tamanho dele é {self.tamanho} " )
