# TP Validation des acquis 2
# Objectif :
# Créer un programme en Python pour enregistrer des commandes clients, en utilisant :
#     Une classe simple,
#     La gestion des erreurs,
#     Un fichier texte pour sauvegarder.
# 
# Consignes :
#     Créer une classe Commande avec 3 attributs :
#         client (nom du client),
#         produit (nom du produit),
#         quantite (nombre entier strictement positif).
#     Si la quantité est invalide (pas un entier positif), le programme doit lever une exception.
#     Ajouter une méthode afficher() qui retourne la commande sous forme de texte :
#         Exemple : "Client: Alice - Produit: Livre - Quantite: 2"
#     Ajouter une méthode sauvegarder() qui ajoute la commande dans un fichier texte commandes.txt.
#     Créer une fonction charger_commandes() qui affiche toutes les commandes enregistrées dans le fichier.
#     Dans le programme principal :
#         Créer deux commandes valides,
#         Tenter de créer une commande avec une quantité invalide,
#         Sauvegarder les commandes valides,
#         Afficher le contenu du fichier.

import os

CHEMIN = os.path.dirname(__file__)

# Classe qui represente une commande client
class Commande:
    def __init__(self, client, produit, quantite):
        # On verifie que la quantite est un entier positif
        if not isinstance(quantite, int) or quantite <= 0:
            # Si ce n'est pas le cas, on leve une exception de type Exception
            raise Exception("Quantite invalide. Elle doit etre un entier positif.")
        self.client = client
        self.produit = produit
        self.quantite = quantite

    # Methode pour obtenir une chaine de caractere representant la commande
    def afficher(self):
        return "Client: " + self.client + " - Produit: " + self.produit + " - Quantite: " + str(self.quantite)

    # Methode pour sauvegarder la commande dans un fichier texte
    def sauvegarder(self, fichier=CHEMIN + "/commandes.txt"):
        with open(fichier, "a") as f:
            f.write(self.afficher() + "\n")


# Fonction pour lire et afficher toutes les commandes du fichier
def charger_commandes(fichier=CHEMIN + "/commandes.txt"):
    print("Commandes enregistrees :")
    try:
        with open(fichier, "r") as f:
            for ligne in f:
                print(ligne.strip())
    except FileNotFoundError:
        print("Aucune commande trouvee.")

# Fonction principale
def main():
    try:
        print("Creation de la commande 1.")
        c1 = Commande("Alice", "Livre", 2)
        print("Commande 1 creee.")

        print("Creation de la commande 2.")
        c2 = Commande("Bob", "Stylo", 5)
        print("Commande 2 creee.")

        print("Creation de la commande 3.")
        c3 = Commande("Charlie", "Cahier", -1)  # Cette ligne va provoquer une exception

    except Exception as e:
        print("Erreur lors de la creation de la commande :", e)

    # Sauvegarde des commandes valides
    c1.sauvegarder()
    c2.sauvegarder()

    # Affichage des commandes sauvegardees
    charger_commandes()

# Programme principal
if __name__ == "__main__":
    main()
