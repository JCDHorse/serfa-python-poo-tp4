import sys

from ParcError import ParcError, StationError
from parcvelos import ParcDeVelos
from classVelo import Velo
from Station import Station

class Main:
    def __init__(self, parc: ParcDeVelos | None = None):
        if parc is None:
            self.__parc = ParcDeVelos()
        else:
            self.__parc = parc

    # 1.1
    def usr_louer_velo(self):
        print(self.__parc.consulter_parc())
        s_id = input("ID de la station: ").upper()
        hd = int(input("Quelle heure est-il ? (si il es 00h mettre 24h)"))
        ticket = self.__parc.louer_velo(s_id, hd)
        print(f"Vélo {ticket["velo"].get_id()} a été loué a {hd}h a la station {s_id}")

    # 1.2
    def usr_retourner_velo(self):
        print(self.__parc.consulter_parc())
        v_id = input("ID du vélo: ").upper()
        s_id = input("ID de la station: ").upper()
        hf = int(input("Quelle heure est-il ? (si il es 00h mettre 24h)"))
        tarif = self.__parc.retourner_velo(s_id, hf, v_id)
        print(f"Vélo {v_id} a été retourné a {hf}h a la station {s_id}.")
        print(f"Prix de la location : {tarif}€")


    # 2.1
    def consulter(self):
        print(self.__parc.consulter_parc())

    # 2.2
    def ajout_station(self):
        nom = input("Nom de la station: ")
        adresse = input("Adresse de la station: ")
        self.__parc.ajouter_station(Station(nom, adresse))

    # 2.3
    def ajout_velo(self):
        print(self.__parc.consulter_parc())
        s_id = input("ID de la station: ").upper()
        c = int(input("Nombre de vélos a ajouter a la station: "))
        self.__parc.ajouter_new_velos(s_id, c)
        print(f"{c} vélos ajoutés a {s_id}")

    # 2.4
    def retirer_velo(self):
        print(self.__parc.consulter_parc())
        s_id = input("ID de la station: ").upper()
        print(self.__parc.consulter_station(s_id))
        v_id = input("ID du vélo: ").upper()
        self.__parc.retirer_velo(s_id, v_id)

    # 2.5
    def reparer_velo(self):
        print(self.__parc.consulter_parc())
        s_id = input("ID de la station: ").upper()
        print(self.__parc.consulter_station(s_id))
        v_id = input("ID du vélo: ").upper()
        self.__parc.envoyer_en_reparation(s_id, v_id)

    # 2.6
    def reaffecter_velo(self):
        print(self.__parc.consulter_parc())
        s_id = input("ID de la station: ").upper()
        print(self.__parc.consulter_velos_reparations())
        v_id = input("ID du vélo: ").upper()
        self.__parc.reaffecter_velo_repare(s_id, v_id)
        print(f"Vélo {v_id} revenu de réparations et affecté a la station {s_id}")

parc = ParcDeVelos()
s_eiffel = Station("Tour Eiffel", "5 parc du Champ de Mars, 75007 Paris")
print(s_eiffel.ajouter_velo(10))
s_louvre = Station("Louvre", "8 rue Sainte-Anne, 75001 Paris")

parc.ajouter_station(s_eiffel)
parc.ajouter_station(s_louvre)

#ok = parc.louer_velo(s_eiffel.id, 7)
#if ok:
#    print("Vélo loué avec succès")
print("------------------------------------------------------")
print(s_eiffel.afficher_info())
print("------------------------------------------------------")
#velo_id_demade = input("veuillez rentrer votre id, exemple V_1000 : ")

main = Main(parc)

#mis en place du tableau de fonction a deux dimension
tab_fonction = [
    [
        main.usr_louer_velo,        # 1.1
        main.usr_retourner_velo,    # 1.2
    ],
    [
        main.consulter,             # 2.1
        main.ajout_station,         # 2.2
        main.ajout_velo,            # 2.3
        main.retirer_velo,          # 2.4
        main.reparer_velo,          # 2.5
        main.reaffecter_velo,       # 2.6
    ]
]

#menu utilisateur
menu_principal = ("Menu Principal : \n"
                  "1. Utilisateur - Location de vélos\n"    
                  "2. Gestionnaire - Gestion du parc\n"
                  "3. Quitter")

sous_menus = [
   ("\t1 Louer un vélo\n"
    "\t2 Retourner un vélo\n"
    "\t3. Retour au menu principal\n"),
    ("\t1. Consulter l’état du parc\n"
      "\t2. Ajouter une nouvelle station au parc\n"
      "\t3. Ajouter un ou plusieurs vélos dans une station\n"
      "\t4. Retirer un vélo d’une station\n"
      "\t5. Envoyer un vélo en réparation\n"
      "\t6. Réaffecter un vélo réparé à une station\n"
      "\t7. Retour au menu principal\n"),
]

running = True
cat = None

while running:
    try:
        if cat is None:
            print(menu_principal)
            cat = int(input("Veuillez rentrer la categorie souhaité : "))


        if cat > len(tab_fonction) + 1:
            cat = None
            raise ValueError

        if cat == len(tab_fonction) + 1:
            running = False
            break

        print(sous_menus[cat - 1])
        cmd = int(input("Veuillez rentrer la commande souhaitée : "))

        if cmd > len(tab_fonction[cat - 1]) + 1:
            cmd = None
            raise ValueError

        if cmd == len(tab_fonction[cat - 1]) + 1:
            cat = None
            continue

        cmd_f = tab_fonction[cat - 1][cmd - 1]
        cmd_f()

    except ValueError:
        print("Veuillez rentrer une valeur possible.")
        continue
    except StationError as err:
        print(f"Erreur de la station: {err}\n", file=sys.stderr)
    except ParcError as err:
        print(f"Erreur du parc: {err}\n", file=sys.stderr)

