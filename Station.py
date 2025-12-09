from random import randint
from classVelo import Velo


class Station:
    __id_util = []
    def __init__(self, name, adress,capacity=10):
        self.__id = self.generate_id()
        self.__nom = name
        self.__emplacement = adress
        self.__capacite = capacity
        self.__velos = []

    @classmethod
    def generate_id(cls):
        while True:
            id = f"S{randint(3400, 4000)}X"
            if id not in Station.__id_util:
                Station.__id_util.append(id)
                return id

    def ajouter_velo(self,argument):
        if len(self.__velos) == self.__capacite:
            return "veuillez supprimer un velo car la station n'a plus de place."
        else:
            if isinstance(argument, Velo):
                self.__velos.append(argument)
            elif isinstance(argument,int):
                for i in range(argument):
                    self.__velos.append(Velo())
                return f"{argument} velos ont ete ajoutes"

    def retirer_velo(self):
        velo_retire = None
        for velo in self.__velos:
            if velo.get_etat() == "disponible":
                velo_retire =velo
                break

        if velo_retire:
            self.__velos.remove(velo_retire)
            print(f"le velo {velo_retire.get_id} a ete enlever")
            return velo_retire
        else:
            print("aucun velo n'est disponible")
            return None

    def afficher_info(self):
        return (f"Voici la station : {self.__nom}\n"
                f"l'adresse : {self.__emplacement}\n"
                f"la capacite : {self.__capacite}\n"
                f"et le nombre de velo actuel : {len(self.__velos)}")

    @property
    def emplacement(self):
        return self.__emplacement

    @emplacement.setter
    def emplacement(self,nvl_emplacement):
        self.__emplacement = nvl_emplacement
    
    @property
    def velos(self):
        return self.__velos

    @property
    def nom(self):
        return self.__nom

    @property
    def id(self):
        return self.__id
