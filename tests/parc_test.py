import unittest

from ParcDeVelos import ParcDeVelos
from Station import Station
from Velo import Velo
from ParcError import ParcError


class ParcDeVelosTest(unittest.TestCase):
    def setUp(self):
        self.parc = ParcDeVelos()
        self.station = Station("ParcTest", "3 boulevard", capacity=5)
        # ajouter 3 vélos
        self.station.ajouter_velo(3)
        self.parc.ajouter_station(self.station)

    def test_calculer_tarif_horaires(self):
        # 8->10 (de 8 à 9 et 9 à 10) : 2 heures en journée (2€/h)
        t = ParcDeVelos.calculer_tarif(8, 10)
        self.assertEqual(t, 4)
        # 0->6 : 6 heures creuses (1€/h)
        self.assertEqual(ParcDeVelos.calculer_tarif(0, 6), 6)
        # 16->18 : 16->17 (2€), 17->18 (1€) => 3
        self.assertEqual(ParcDeVelos.calculer_tarif(16, 18), 3)
        # loc_fin < loc_debut => erreur
        with self.assertRaises(ValueError):
            ParcDeVelos.calculer_tarif(10, 8)

    def test_louer_et_retourner_velo(self):
        # louer un vélo
        ticket = self.parc.louer_velo(self.station.id, 9)
        self.assertIn("debut", ticket)
        self.assertIn("velo", ticket)
        self.assertIn("id", ticket)
        v_id = ticket["id"]
        # retourner le vélo à 11
        price = self.parc.retourner_velo(self.station.id, 11, v_id)
        self.assertIsInstance(price, int)
        self.assertEqual(price, ParcDeVelos.calculer_tarif(9, 11))

    def test_retourner_velo_inconnu_raises(self):
        with self.assertRaises(ParcError):
            self.parc.retourner_velo(self.station.id, 12, "V_0_non_existant")

    def test_envoyer_et_reaffecter_reparation(self):
        # envoyer un vélo en réparation
        # on retire un vélo disponible
        ticket = self.parc.louer_velo(self.station.id, 10)
        v = ticket["velo"]
        # maintenant on renvoie ce vélo dans la station, puis on envoie en réparation
        self.parc.retourner_velo(self.station.id, 11, v.id)
        # envoyer en réparation
        self.parc.envoyer_en_reparation(self.station.id, v.id)
        # tente de réaffecter
        self.parc.reaffecter_velo_repare(self.station.id, v.id)

    def test_consulter_parc_et_station(self):
        info = self.parc.consulter_parc()
        self.assertIn("Voici la station", info)
        s_info = self.parc.consulter_station(self.station.id)
        self.assertIn(self.station.nom, s_info)


if __name__ == '__main__':
    unittest.main()

