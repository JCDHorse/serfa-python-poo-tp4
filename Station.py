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
            if id not in cls.__id_util:
                cls.__id_util.append(id)
                return id

    def ajouter_velo(self,argument):
        # Si plus de capacité de stockage alors on return
        if len(self.__velos) == self.__capacite:
            return "station pleine : impossible d'ajouter un nouveau vélo."

        else:
            # On ajoute un seul vélo
            if isinstance(argument, Velo):
                if len(self.__velos) < self.__capacite:
                    self.__velos.append(argument)
                    return "1 vélo ajouté."
                return "station pleine : impossible d'ajouter un nouveau vélo."
            
            # On ajoute plusieurs vélos
            elif isinstance(argument,int):
                ajout_velo=0
                for i in range(argument):
                    if len(self.__velos) < self.__capacite:
                        self.__velos.append(Velo())
                        ajout_velo+=1
                    else:
                        break
                return f"{ajout_velo} vélos ont été ajoutés sur {argument}"

    def retirer_velo(self):
        velo_retire = None
        for velo in self.__velos:
            if velo.get_etat() == "disponible":
                velo_retire =velo
                break

        if velo_retire:
            self.__velos.remove(velo_retire)
            print(f"le vélo {velo_retire.get_id()} a été retiré")
            return velo_retire
        else:
            print("aucun vélo n'est disponible")
            return None

    def afficher_info(self):
        return (f"Voici la station : {self.__nom}\n"
                f"l'adresse : {self.__emplacement}\n"
                f"la capacité : {self.__capacite}\n"
                f"et le nombre de vélo actuel : {len(self.__velos)}")

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


