import unittest
from src.elementy import Blenda


class BlendaTest(unittest.TestCase):
    def test_dlugosc_tylu_dla_jednej_blendy(self):
        blenda = Blenda(box=1, szerokosc_garazu=3000)
        self.assertEqual(blenda.dlugosc_tyl(), 3040)

    def test_dlugosc_tylu_dla_wielu_blend(self):
        blenda = Blenda(box=1, szerokosc_garazu=4000)
        self.assertEqual(blenda.dlugosc_tyl(), 2050)

    # def test_dlugosc_tylu_wiele_boxow(self):
    #     blenda = Blenda(box=3, szerokosc_garazu=4000)
    #     self.assertEquals(blenda.dlugosc_tyl(),


def main():
    unittest.main()


if __name__ == '__main__':
    main()
