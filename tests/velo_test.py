import unittest

from Velo import Velo, VeloEtat


class VeloTest(unittest.TestCase):
    velos = [Velo(), Velo(), Velo()]

    def test_velo(self):
        for v in VeloTest.velos:
            self.assertEqual(v.etat, VeloEtat.DISPONIBLE)

    def test_reparation(self):
        velo = VeloTest.velos[0]
        velo.a_reparer()
        self.assertEqual(velo.etat, VeloEtat.REPARATION)
        velo.mettre_en_location()
        self.assertEqual(velo.etat, VeloEtat.REPARATION)
        velo.terminer_reparation()
        self.assertEqual(velo.etat, VeloEtat.DISPONIBLE)

    def test_location(self):
        velo = VeloTest.velos[1]
        velo.mettre_en_location()
        self.assertEqual(velo.etat, VeloEtat.LOUEE)
        velo.retourner()
        self.assertEqual(velo.etat,  VeloEtat.DISPONIBLE)

if __name__ == '__main__':
    unittest.main()
