from src.elementy import Blenda

garaz = {
    'box': 1,
    'szerokosc_garazu': 3000,
    'dlugosc_garazu': 4000,
    }

blenda = Blenda(**garaz)
blenda.wypisz_blendy()
