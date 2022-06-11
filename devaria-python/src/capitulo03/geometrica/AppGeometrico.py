from src.capitulo03.geometrica.FormaGeometrica import FormaGeometrica
from src.capitulo03.geometrica.Quadrado import Quadrado
from src.capitulo03.geometrica.Circulo import Circulo

formas = [
    Quadrado(),
    Circulo()
]

for forma in formas:
    forma.Desenhar()
