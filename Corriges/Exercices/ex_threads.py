# Exercice Threads
# 
# On veut écrire un programme qui : Lance 3 threads en parallèle.
# Chaque thread doit afficher son nom et compter de 1 à 5, avec une pause d’1 seconde entre chaque nombre.
# Le programme principal doit attendre la fin de tous les threads avant d’afficher "Programme terminé".

# Imports
import threading
import time

def compter():
    """
    Fonction exécutée par chaque thread
    """
    for i in range(1, 6):
        print(f"{threading.current_thread().name} : {i}")
        time.sleep(1)

# Créer une liste de threads
threads: list[threading.Thread] = []

# Execute les 3 threads et les ajoutent a la liste des threads.
for n in range(3):
    t = threading.Thread(target=compter, name=f"Thread-{n+1}")
    threads.append(t)
    t.start()

# Attendre que tous les threads se terminent
for t in threads:
    t.join()

print("Programme terminé.")
