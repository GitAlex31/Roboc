# -*-coding:Utf-8 -*

"""Ce module contient la classe Carte."""
from labyrinthe import Labyrinthe


class Carte:

    """Objet de transition entre un fichier et un labyrinthe."""

    def __init__(self, nom, fichier):
        self.nom = nom
        self.labyrinthe = Labyrinthe(fichier)

    def __repr__(self):
        return "<Carte {}>".format(self.nom)
