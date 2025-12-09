from datetime import datetime

class ParcDeVelos:
    def __init__(self):
        self._stations = []
        self._en_locations = []
        self._en_reparations = []


    def get_stations(self) -> list:
        return self._stations

    def get_en_reparations(self):
        return self._en_reparations

    def get_en_locations(self):
        return self._en_locations

    def ajouter_station(self, station):
        self._stations.append(station)

    def louer_velo(self, station, loc_debut: datetime):
        ...

    def envoyer_en_reparation(self, v_id: str):
        ...

    def consulter_parc(self):
        for station in self._stations:
            station.afficher_info()



    stations = property(fget=get_stations)
    en_reparation = property(fget=get_en_reparations)
    en_locations = property(fget=get_en_locations)
