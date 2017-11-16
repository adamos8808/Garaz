class Base:
    def __init__(self, **kwargs):
        self.box = kwargs.get('box')
        self.szerokosc_garazu = kwargs.get('szerokosc_garazu')
        self.dlugosc_garazu = kwargs.get('dlugosc_garazu')

    @staticmethod
    def mround(number, mulitple=50):
        return int(mulitple * round(float(number) / mulitple))
