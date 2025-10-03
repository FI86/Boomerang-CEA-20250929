# Deux acheteurs ajoutant des articles à un bloc-notes partagé.

# Il est possible qu'une valeur soit ecrasée par un autre threads.
# Cette exemple dépend aussi de la vitesse du PC. avec certains, ca passe bien,
# avec d'autre on voit le data race car le nombre de crayons totaux
# n'est pas correcte.
from threading import Thread

crayons = 0

def acheteur():
    global crayons

    for _ in range(10_000_000):
        crayons += 1

def main():
    barron = Thread(target = acheteur)
    olivia = Thread(target = acheteur)
    barron.start()
    olivia.start()
    barron.join()
    olivia.join()
    print(f"Nous devons acheter {crayons} de crayons.")

if __name__ == '__main__':
    main()
