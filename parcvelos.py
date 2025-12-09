from Station import Station
from classVelo import Velo

class ParcDeVelos:
    def __init__(self):
        self._stations = dict()
        self._en_locations = []
        self._en_reparations = []

    def trouve_velo(self, v_id: str) -> Velo | None:
        velo: Velo | None = None
        for station in self._stations:
            for s_velo in station.velos:
                if s_velo.get_id() == v_id:
                    velo = s_velo
                    break
        return velo

    def calculer_tarif(self, loc_debut: int, loc_fin: int) -> int:
        price = 0
        if loc_fin < loc_debut:
            raise ValueError("Impossible de louer en remontant dans le passé")
        for i in range(loc_debut, loc_fin):
            if (0 <= i < 7) or (17 <= i < 24):
                price += 1
            elif 7 <= i < 17:
                price += 2
        return price

    def creer_station(self, name: str, address: str, capacity: int = 10):
        station = Station(name, address, capacity)
        self._stations[station.id] = station

    def ajouter_station(self, station: Station):
        self._stations[station.id] = station

    def louer_velo(self, s_id: str, loc_debut: int):
        velo = self._stations[s_id].retirer_velo()
        self._en_locations.append(velo)

    def retourner_velo(self, v_id: str, loc_fin: int) -> bool:
        velo = self.trouve_velo(v_id)

        if velo is None:
            return False

        velo.retourner()
        self._en_locations.remove(velo)
        return True

    def ajouter_new_velos(self, s_id: str, nv: int):
        self._stations[s_id].ajouter_velo(nv)

    def envoyer_en_reparation(self, v_id: str) -> bool:
        velo = self.trouve_velo(v_id)

        if velo is None:
            return False

        velo.a_reparer()
        self._en_reparations.append(velo)
        return True

    def reaffecter_velo_repare(self, v_id: str) -> bool:
        velo = self.trouve_velo(v_id)

        if velo is None:
            return False

        velo.terminer_reparation()
        self._en_reparations.remove(velo)
        return True

    def consulter_parc(self):
        infos = ""
        for station in self._stations:
            infos += station.afficher_info()
        return infos
