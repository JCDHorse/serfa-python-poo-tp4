from Station import Station
from classVelo import Velo

class ParcDeVelos:
    def __init__(self):
        self.__stations = dict()
        self.__en_locations = []
        self.__en_reparations = []

    def trouve_velo(self, v_id: str) -> Velo | None:
        velo: Velo | None = None
        for station in self.__stations:
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
        self.__stations[station.id] = station

    def ajouter_station(self, station: Station):
        self.__stations[station.id] = station

    def louer_velo(self, s_id: str, loc_debut: int):
        velo = self.__stations[s_id].retirer_velo()
        if velo is None:
            return False
        self.__en_locations.append(velo)
        return True

    def retourner_velo(self, v_id: str, loc_fin: int) -> bool:
        velo = self.trouve_velo(v_id)

        if velo is None:
            return False

        velo.retourner()
        self.__en_locations.remove(velo)
        return True

    def ajouter_new_velos(self, s_id: str, nv: int):
        self.__stations[s_id].ajouter_velo(nv)

    def envoyer_en_reparation(self, v_id: str) -> bool:
        velo = self.trouve_velo(v_id)

        if velo is None:
            return False

        velo.a_reparer()
        self.__en_reparations.append(velo)
        return True

    def reaffecter_velo_repare(self, v_id: str) -> bool:
        velo = self.trouve_velo(v_id)

        if velo is None:
            return False

        velo.terminer_reparation()
        self.__en_reparations.remove(velo)
        return True

    def consulter_parc(self):
        infos = ""
        for station in self.__stations:
            infos += station.afficher_info()
        return infos
