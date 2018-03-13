# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinthe."""

class Labyrinthe:

    """Classe représentant un labyrinthe."""

    def __init__(self, fichier):

        # initialisation de la grille
        contenu = fichier.readlines()
        num_char = len(contenu[0]) - 1  # on enlève le caractère saut de ligne
        nb_lignes = len(contenu)

        self.grille = list()
        for i in range(num_char):
            self.grille.append(-1)  # Attention : le fait d'effectuer [-1] * num_char créée une liste non-mutable
        self.grille = [list(self.grille) for self.grille in [self.grille] * nb_lignes]  # On créée encore des listes mutables

        # remplissage de la grille
        for i, ligne in enumerate(contenu):
            for j, char in enumerate(ligne):
                if char != '\n':
                    self.grille[i][j] = char
        print(self)

    def deplacer_robot(self):
        """Déplace le robot représenté sous forme de croix dans le labyrinthe.
        Il ne peut pas se déplacer à travers les murs ni sortir de la carte.
        #TODO : contôler avec des erreurs les sorties de la carte"""
        #  on trouve d'abord la position initiale du robot
        for i, ligne in enumerate(self.grille):
            for j, caractere in enumerate(ligne):
                if self.grille[i][j] == 'X':
                    coord_init = i, j

        direction = input("Veuillez entrer la direction de déplacement du robot (N/S/E/O).")
        nb_cases = input("Puis le nombre de cases de déplacement.")
        nb_cases = int(nb_cases)

        if direction == 'N':
            coord_traversees = [(i, coord_init[1]) for i in range(coord_init[0] - nb_cases, coord_init[0])]
            coord_finales = coord_traversees[0]
        elif direction == 'S':
            coord_traversees = [(i, coord_init[1]) for i in range(coord_init[0], coord_init[0] + nb_cases + 1)]
            coord_finales = coord_traversees[-1]
        elif direction == 'E':
            coord_traversees = [(coord_init[0], j) for j in range(coord_init[1], coord_init[1] + nb_cases + 1)]
            coord_finales = coord_traversees[-1]
        elif direction == 'O':
            coord_traversees = [(coord_init[0], j) for j in range(coord_init[1] - nb_cases, coord_init[1])]
            coord_finales = coord_traversees[0]
        else:
            raise ValueError("Veuillez entrer une direction valable.")

        for coord in coord_traversees:
            if 'O' in self.grille[coord[0]][coord[1]]:
                raise ValueError("Impossible de se déplacer à travers les murs !")

            if 'U' in self.grille[coord[0]][coord[1]]:
                print("Félicitations ! Vous avez gagné la partie.")
                raise KeyboardInterrupt

        # On enlève le robot aux coordonnées initiales
        self.grille[coord_init[0]][coord_init[1]] = " "

        # Pour le déplacer aux nouvelles coordonnées
        self.grille[coord_finales[0]][coord_finales[1]] = "X"

        print(self)

    def __str__(self):
        str_repr = str()
        for i, ligne in enumerate(self.grille):
            for j, char in enumerate(ligne):
                str_repr += char
            str_repr += '\n'
        return str_repr

if __name__ == "__main__":
    pass