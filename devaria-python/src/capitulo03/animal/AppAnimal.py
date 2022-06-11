# herança
from src.capitulo03.Animal import Animal
from src.capitulo03.Mamifero import Mamifero
from src.capitulo03.Reptil import Reptil

if __name__ == '__main__':
    animal = Animal( 'leão', 1.8 )
    animal.respirar ()

    mamifero = Mamifero( 'vaca', 2.5 )
    mamifero.respirar ()
    mamifero.Alimentar ()

    reptil = Reptil( "Jacaré", 3.9 )
    reptil.respirar ()
    reptil.BotaOvo ()
