from math import floor, ceil
from src.elementy import element


class Blenda(element.Base):
    MAX_DL_BLENDY = 4000
    NAKLADKA = 50
    NAKLADKA_NA_BOK = 150
    NAKLADKA_NA_TYL = 40
    NAKLADKA_POJEDYNCZA_BLENDA_BOK = 200

    def dlugosc_przod(self):
        ilosc = floor(self.ilosc_pt())
        wynik = (self.szerokosc_garazu / ilosc) + self.NAKLADKA
        return self.mround(wynik)

    def ilosc_pt(self):
        sn = self.szerokosc_garazu + self.NAKLADKA
        return ceil(sn / self.MAX_DL_BLENDY)

    def dlugosc_boku(self) -> int:
        ilosc = floor(self.ilosc_boku())
        if int(ilosc) == 1 and int(self.box) == 1:
            wynik = self.dlugosc_garazu / ilosc + self.NAKLADKA_POJEDYNCZA_BLENDA_BOK
        else:
            ilosc = floor(self.ilosc_boku())
            wynik = self.dlugosc_garazu / ilosc + self.NAKLADKA_NA_BOK
            wynik = self.mround(wynik)
        return wynik

    def ilosc_boku(self):
        dn = self.dlugosc_garazu + self.NAKLADKA_NA_BOK
        return ceil(dn / self.MAX_DL_BLENDY)

    def dlugosc_tyl(self) -> int:
        ilosc = floor(self.ilosc_pt())
        if ilosc == 1 and self.box == 1:
            wynik = self.szerokosc_garazu / ilosc + self.NAKLADKA_NA_TYL
            wynik = self.mround(wynik, 40)
        else:
            wynik = self.szerokosc_garazu / ilosc + self.NAKLADKA
            wynik = self.mround(wynik)
        return wynik

    def wypisz_blendy(self) -> str:
        sep = " "
        br = "\n"
        print("Blendy przód: {0}{1}{2}{3}Blendy boki: {4}{5}{6}{7}Blendy tył: {8}{9}".format(str(self.ilosc_pt() * self.box), sep,
                                                                                         str(self.dlugosc_przod()), br,
                                                                                         str(self.ilosc_boku()), sep,
                                                                                         str(self.dlugosc_boku()), br,
                                                                                         str(self.ilosc_pt() * self.box) + sep,
                                                                                         str(self.dlugosc_tyl())))
