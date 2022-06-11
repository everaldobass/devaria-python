from src.capitulo03.Animal import Animal

class Reptil ( Animal ):
    def __int__(self, nome: object, tamanho: object):
        super ().__int__ ( nome, tamanho )

    def BotaOvo(self):
        print ( f"O animal{self.nome} está botando ovo. O tamanho dele é {self.tamanho}" )
