from parcvelos import ParcDeVelos
from classVelo import Velo
from Station import Station

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

#creation des variables
velo_id_demande = "0"
heureDebut = 0
heureFin = 0
station_prise = s_eiffel
valeur_autoriser = ["1","2","3","4","5","6","7","quitter"]
nom_station = "oui"
adress_station = "oui"
capacity_station = 10
nombre_velo = 1
parc_choisi = parc

#mis en place du tableau de fonction a deux dimension
tab_fonction = [[parc_choisi.louer_velo(station_prise.id,heureDebut), #1 1
                 parc_choisi.retourner_velo(station_prise.id,heureFin,velo_id_demande)], #1 2

                [parc_choisi.consulter_parc(), #2 1
                 parc_choisi.ajouter_station(Station(nom_station,adress_station,capacity_station)), #2 2
                 station_prise.ajouter_velo(nombre_velo),#2 3
                 station_prise.retirer_velo(), #2 4
                 parc_choisi.envoyer_en_reparation(velo_id_demande),#2 5
                 parc_choisi.reaffecter_velo_repare(velo_id_demande) #2 6
                 ]]

#menu utilisateur
menu_principal = ("Menu Principal : \n"
                  "1. Utilisateur - Location de vélos\n"    
                  "2. Gestionnaire - Gestion du parc\n"
                  "Quitter")

sous_menu1 = ("\t1 Louer un vélo\n"
              "\t2 Retourner un vélo\n"
              "\t3. Retour au menu principal\n"
              "Quitter\n")

sous_menu2 = ("\t1. Consulter l’état du parc\n"
              "\t2. Ajouter une nouvelle station au parc\n"
              "\t3. Ajouter un ou plusieurs vélos dans une station\n"
              "\t4. Retirer un vélo d’une station\n"
              "\t5. Envoyer un vélo en réparation\n"
              "\t6. Réaffecter un vélo réparé à une station\n"
              "\t7. Retour au menu principal\n"
              "Quitter\n")



while True:
    print(menu_principal)
    try:
        cate = input("veuillez rentrer la categorie souhaité : ")
        if cate != "quitter" and cate in ["1","2","3"]:
            cate = int(cate)
            if cate > 3 or cate <1:
                print("il faut que le premier soit soit 1 ou bien 2")
                continue
            elif cate == 1 :
                print(sous_menu1)
                sous_cate = input("veuillez rentrer la sous catégorie souhaité : ")
                if sous_cate not in ["1","2","quitter"]:
                    raise ValueError
                else :
                    sous_cate = int(sous_cate)
                    print(tab_fonction[cate][sous_cate])

            elif cate ==2:
                print(sous_menu2)
                sous_cate = input("veuillez rentrer la sous catégorie souhaité : ")
                if sous_cate not in ["1","2","3","4","5","6","7","quitter"]:
                    raise ValueError
                else :
                    sous_cate = int(sous_cate)
                    print(tab_fonction[cate][sous_cate])
            else:
                continue

        elif cate not in ["1","2","quitter"]:
            raise ValueError

        else:
            print("Vous venez de quitter")
            break
    except ValueError:
        print("veuillez rentrer une valeur possible.")
        continue

