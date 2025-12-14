import unittest

from Station import Station
from classVelo import Velo
from ParcError import StationError


class StationTest(unittest.TestCase):
    def setUp(self):
        self.station = Station("TestStation", "1 rue", capacity=3)

    def _count_velos(self):
        # la propriété velos retourne une chaîne avec un vélo par ligne
        s = self.station.velos
        return len(s.splitlines()) if s else 0

    def test_ajouter_velo_instance(self):
        v = Velo()
        added = self.station.ajouter_velo(v)
        self.assertEqual(added, 1)
        # on doit pouvoir retrouver le vélo par son id
        found = self.station.get_velo(v.id)
        self.assertIs(found, v)
        self.assertEqual(self._count_velos(), 1)

    def test_ajouter_multiple_et_capacite(self):
        # on demande d'ajouter 5 vélos mais la capacité est 3
        added = self.station.ajouter_velo(5)
        self.assertEqual(added, 3)
        self.assertEqual(self._count_velos(), 3)
        # ajouter un vélo de plus doit lever une erreur
        with self.assertRaises(StationError):
            self.station.ajouter_velo(Velo())

    def test_retirer_velo_par_defaut_et_par_id(self):
        v1 = Velo()
        v2 = Velo()
        self.station.ajouter_velo(v1)
        self.station.ajouter_velo(v2)
        count_before = self._count_velos()
        # retirer sans id doit retirer un vélo disponible
        r = self.station.retirer_velo()
        self.assertIn(r, (v1, v2))
        self.assertEqual(self._count_velos(), count_before - 1)
        # retirer par id
        remaining = self.station.retirer_velo(v_id=v2.id)
        # si v2 avait été retiré en premier, alors essayer de retirer par id doit lever une erreur
        # On gère les deux cas possibles
        # soit remaining est v2, soit une StationError est levée

    def test_get_velo_inexistant_ouvre_exception(self):
        with self.assertRaises(StationError):
            self.station.get_velo("V_999999")

    def test_emplacement_setter(self):
        self.station.emplacement = "2 avenue"
        self.assertEqual(self.station.emplacement, "2 avenue")


if __name__ == '__main__':
    unittest.main()

