import abc

class FormaGeometrica(abc.ABC):
    def __int__(self):
        pass
    @abc.abstractmethod
    def Desenhar(self):
        pass
