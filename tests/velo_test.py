import unittest

from classVelo import Velo

class VeloTest(unittest.TestCase):
    velos = [Velo(), Velo(), Velo()]

    def test_velo(self):
        for v in VeloTest.velos:
            self.assertEqual(v.get_etat(), "disponible")

    def test_reparation(self):
        velo = VeloTest.velos[0]
        velo.a_reparer()
        self.assertEqual(velo.get_etat(), "en_reparation")
        velo.mettre_en_location()
        self.assertEqual(velo.get_etat(), "en_reparation")
        velo.terminer_reparation()
        self.assertEqual(velo.get_etat(), "disponible")

    def test_location(self):
        velo = VeloTest.velos[1]
        velo.mettre_en_location()
        self.assertEqual(velo.get_etat(), "en_location")
        velo.retourner()
        self.assertEqual(velo.get_etat(), "disponible")

if __name__ == '__main__':
    unittest.main()
