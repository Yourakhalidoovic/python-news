class Cellule:
    def __init__(self, est_vivante=False):
        self.vivante = est_vivante

    def est_vivante(self):
        return self.vivante

    def mettre_a_jour(self, nombre_voisins_vivants):
        # Appliquer les règles du jeu de la vie
        if self.vivante:
            if nombre_voisins_vivants < 2 or nombre_voisins_vivants > 3:
                self.vivante = False
        else:
            if nombre_voisins_vivants == 3:
                self.vivante = True
class Grille:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.grille = [[Cellule() for _ in range(largeur)] for _ in range(hauteur)]

    def afficher(self):
        pass
        # Méthode pour afficher la grille (par exemple, en utilisant des caractères)

    def evoluer(self):
        # Méthode pour calculer le nombre de voisins vivants pour chaque cellule
        # et mettre à jour l'état de chaque cellule
        nouvelle_grille = [[Cellule() for _ in range(self.largeur)] for _ in range(self.hauteur)]
        # ... (implémentation des calculs et mise à jour)
        self.grille = nouvelle_grille
# Créer une grille de taille 10x10
grille = Grille(10, 10)

# Initialiser aléatoirement quelques cellules
# ...

# Boucle principale
while True:
    grille.afficher()
    grille.evoluer()
    # Ajouter un délai pour visualiser l'évolution