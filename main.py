from parcvelos import ParcDeVelos
from classVelo import Velo
from Station import Station

parc = ParcDeVelos()
s_eiffel = Station("Tour Eiffel", "5 parc du Champ de Mars, 75007 Paris")
s_eiffel.ajouter_velo(10)
s_louvre = Station("Louvre", "8 rue Sainte-Anne, 75001 Paris")

parc.ajouter_station(s_eiffel)
parc.ajouter_station(s_louvre)

ok = parc.louer_velo(s_eiffel.id, 7)
if ok:
    print("Vélo loué avec succès")
