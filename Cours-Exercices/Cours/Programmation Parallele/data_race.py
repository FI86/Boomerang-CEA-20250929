# Deux acheteurs ajoutant des articles à un bloc-notes partagé.

# Il est possible qu'une valeur soit ecrasée par un autre threads.
# Cette exemple dépend aussi de la vitesse du PC. avec certains, ca passe bien,
# avec d'autre on voit le data race car le nombre de crayons totaux
# n'est pas correcte.
def acheteur():
    pass

if __name__ == '__main__':
    pass