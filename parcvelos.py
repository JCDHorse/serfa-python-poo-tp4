from Station import Station
from classVelo import Velo

class ParcDeVelos:
    def __init__(self):
        self.__stations = dict()
        self.__en_locations = []
        self.__en_reparations = []

    def ajouter_station(self, station: Station):
        self.__stations[station.id] = station
    
    def louer_velo(self, s_id: str, loc_debut: int):
        velo_loue = self.__stations[s_id].retirer_velo()
        if velo_loue is None:
            return False
        ticket = {"debut":loc_debut, "velo":velo_loue, "id": velo_loue.id}
        self.__en_locations.append(ticket)
        return True

    def retourner_velo(self, s_id: str, loc_fin: int, v_id:str) -> bool:
        ticket=None
        for t in self.__en_locations:
            if t["id"]==v_id:
                ticket = t
                break
            
        if ticket is None:
            return False

        velo_retour=ticket["velo"]
        loc_deb=ticket["debut"]

        self.__en_locations.remove(ticket)
        velo_retour.retourner()

        self.ajouter_new_velos(s_id, velo_retour)

        tarif=self.calculer_tarif(loc_deb, loc_fin)
        return tarif
    
    def ajouter_new_velos(self, s_id: str, nv: Velo):
        self.__stations[s_id].ajouter_velo(nv)

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
