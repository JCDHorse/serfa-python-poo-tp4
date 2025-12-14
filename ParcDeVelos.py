from typing import Any

from Station import Station
from Velo import Velo
from ParcError import StationError, ParcError

class ParcDeVelos:
    def __init__(self):
        self.__stations: dict[str, Station] = dict()
        self.__en_locations: list[dict[str, Any]] = []
        self.__en_reparations: list[Velo] = []

    @staticmethod
    def calculer_tarif(loc_debut: int, loc_fin: int) -> int:
        price = 0
        if loc_fin < loc_debut:
            raise ValueError("Impossible de louer en remontant dans le passé")
        for i in range(loc_debut, loc_fin):
            if (0 <= i < 7) or (17 <= i < 24):
                price += 1
            elif 7 <= i < 17:
                price += 2
        return price

    # Méthodes privées utilitaires
    def __station(self, s_id) -> Station:
        if s_id not in self.__stations:
            raise ParcError(f"Station {s_id} n'existe pas")
        return self.__stations[s_id]

    def __trouver_velo(self, s_id: str, v_id: str) -> Velo | None:
        s: Station = self.__station(s_id)
        v = s.get_velo(v_id)
        return v

    # Méthodes publiques
    def ajouter_station(self, station: Station):
        self.__stations[station.id] = station
    
    def louer_velo(self, s_id: str, loc_debut: int) -> dict:
        velo_loue = self.__station(s_id).retirer_velo()
        ticket = {"debut":loc_debut, "velo":velo_loue, "id": velo_loue.id}
        self.__en_locations.append(ticket)
        return ticket

    def retourner_velo(self, s_id: str, loc_fin: int, v_id:str) -> int:
        ticket: dict | None = None
        for t in self.__en_locations:
            if t["id"] == v_id:
                ticket = t
                break
            
        if ticket is None:
            raise ParcError(f"Le velo {v_id} n'est pas en location")

        velo_retour: Velo = ticket["velo"]
        loc_deb=ticket["debut"]

        self.__en_locations.remove(ticket)
        velo_retour.retourner()

        self.ajouter_new_velos(s_id, velo_retour)

        tarif=self.calculer_tarif(loc_deb, loc_fin)
        return tarif
    
    def ajouter_new_velos(self, s_id: str, nv: Velo | int):
        self.__station(s_id).ajouter_velo(nv)

    def envoyer_en_reparation(self, s_id: str, v_id: str):
        velo = self.__station(s_id).retirer_velo(v_id)
        velo.a_reparer()
        self.__en_reparations.append(velo)

    def reaffecter_velo_repare(self, s_id: str, v_id: str):
        velo = None
        for v in self.__en_reparations:
            if v.id == v_id:
                velo = v
        if velo is None:
            raise ParcError(f"Vélo {v_id} n'est pas en réparation")
        velo.terminer_reparation()
        self.__en_reparations.remove(velo)
        self.ajouter_new_velos(s_id, velo)

    def retirer_velo(self, s_id, v_id):
        s: Station = self.__station(s_id)
        # v => poubelle
        v: Velo = s.retirer_velo(v_id)
        if v is None:
            raise ParcError(f"Vélo {v_id} introuvable sur la station {s_id}")

    def consulter_parc(self):
        infos = ""
        for s in self.__stations.values():
            if isinstance(s, Station):
                infos += s.afficher_info()
        return infos

    def a_velos_reparation(self) -> bool:
        return len(self.__en_reparations) != 0

    def consulter_velos_reparations(self):
        infos = "Vélos en réparation:\n"
        for v in self.__en_reparations:
            infos += "\t- " + v.id + "\n"
        return infos

    def consulter_station(self, s_id: str):
        infos = ""
        s = self.__station(s_id)
        infos += s.afficher_info()
        infos += s.velos
        return infos

if __name__ == '__main__':
    velo1 = Velo()
    velo2 = Velo()
    station = Station("jenesaispas", "10 rue des clochard", 12)
    print(station.ajouter_velo(velo1))
    print("---------------------------------------------------------")
    print(station.ajouter_velo(velo2))
    print("---------------------------------------------------------")
    parc = ParcDeVelos()
    parc.ajouter_station(station)
    parc.louer_velo(str(station.id),8)
    parc.consulter_parc()
    velo_id_demade = input("veuillez rentrer votre id, exemple V_1000 : ")
    print(f"le prix que vous devez payer est de : {parc.retourner_velo(str(station.id),17,str(velo_id_demade))}")
