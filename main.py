from src.elementy import Blenda

garaz = {
    'box': 7,
    'szerokosc_garazu': 4000,
    'dlugosc_garazu': 4000,
    }

blenda = Blenda(**garaz)
blenda.wypisz_blendy()

