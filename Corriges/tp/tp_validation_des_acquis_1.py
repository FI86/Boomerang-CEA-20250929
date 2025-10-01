# TP validation des acquis 1
# 
# Créer un petit programme interactif de gestion de notes pour un élève.
# Le programme devra permettre de :
#   - Demander à l’utilisateur combien de notes il veut entrer.
#   - Saisir ces notes une par une (entre 0 et 20) et les ajouter dans une liste.
#   - Calculer la moyenne de ces notes via une fonction nommée "calcul_moyenne".
#   - Afficher un message différent selon la moyenne :
#           Moins de 10 : "En difficulté"
#           Entre 10 et 15 : "Peut mieux faire"
#           15 ou plus : "Très bien"

def calcul_moyenne(notes: list) -> float:
    # Cette fonction calcule la moyenne d'une liste de notes.
    return sum(notes) / len(notes)

# Fonction principale
def main():
    # Liste vide pour stocker les notes.
    notes = []

    # Demande combien de notes l'utilisateur souhaite entrer.
    while True:
        try:
            nb_notes = int(input("Combien de notes voulez-vous entrer ? "))
            break
        except ValueError:
            print("Erreur. Entrez un nombre.")
    
    # Boucle pour saisir chaque note.
    for i in range(nb_notes):
        while True:
            try:
                note = float(input(f"Entrez la note {i + 1} : "))
            except ValueError:
                print("Note invalide. La note doite etre un nombre.")
            else:
                if 0 <= note <= 20:
                    # Ajoute la note si elle est valide.
                    notes.append(note)
                    break
                else:
                    # Affiche un message si la note est invalide.
                    print("Note invalide. Veuillez entrer une note entre 0 et 20.")

    # Appelle la fonction pour calculer la moyenne.
    moyenne = calcul_moyenne(notes)

    # Affiche la moyenne avec deux chiffres apres la virgule.
    print(f"Moyenne : {moyenne:.2f}")

    # Conditions pour afficher l'appreciation.
    if moyenne < 10:
        print("Appreciation : En difficulte")
    elif moyenne < 15:
        print("Appreciation : Peut mieux faire")
    else:
        print("Appreciation : Tres bien")

# Programme principal
if __name__ == "__main__":
    main()
