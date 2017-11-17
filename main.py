from src.elementy import Blenda

garaz = {
    'box': 3,
    'szerokosc_garazu': 4000,
    'dlugosc_garazu': 4000,
    }

blenda = Blenda(**garaz)
blenda.wypisz_blendy()
