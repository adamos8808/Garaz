import unittest
from src.elementy import Blenda


class BlendaTestCase(unittest.TestCase):
    def dlugosc_tyl_test(self):
        blenda = Blenda(szerokosc_garazu=3000, dlugosc_garazu=4000)
        dl_tyl = blenda.dlugosc_tyl()
        self.assertEqual(dl_tyl, 3040)

unittest.main()
