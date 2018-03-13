# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os

from carte import Carte

# On charge les cartes existantes
cartes = []
for nom_fichier in os.listdir("cartes"):
    if nom_fichier.endswith(".txt"):
        chemin = os.path.join("cartes", nom_fichier)
        nom_carte = nom_fichier[:-3].lower()
        with open(chemin, "r") as fichier:
            #print(fichier.read())
            carte = Carte(nom_carte, fichier)
            cartes.append(carte)

# On affiche les cartes existantes
print("Labyrinthes existants :")
for i, carte in enumerate(cartes):
    print("  {} - {}".format(i + 1, carte.nom))

#num_carte = int(input("Choisissez le numéro de la carte sur laquelle vous voulez jouez."))
num_carte = 1

carte_a_jouer = cartes[num_carte - 1]

quitter = False

while not quitter:

    try:
        carte_a_jouer.labyrinthe.deplacer_robot()
    except ValueError:
        print("Impossible de se déplacer à travers les murs !")
        carte_a_jouer.labyrinthe.deplacer_robot()
    except KeyboardInterrupt:
        quitter = True

# Si il y a une partie sauvegardée, on l'affiche, à compléter


