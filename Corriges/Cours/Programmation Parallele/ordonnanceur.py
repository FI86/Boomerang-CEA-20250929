# 2 threads résolvant des exercices
import threading
import time

resoudreExercice = True

def resolutionExercice():
    nom = threading.current_thread().name
    compteur = 0

    while resoudreExercice:
        print(f"{nom} a resolu un exercice !")
        compteur += 1

    print(f"{nom} a resolu {compteur} exercices.")

if __name__ == '__main__':
    # Démarrage des threads.
    threading.Thread(target=resolutionExercice, name="Toto").start()
    threading.Thread(target=resolutionExercice, name="Titi").start()

    # Délais pour la résolution d'exercices en 1s.
    time.sleep(1)

    # Arrêt des threads.
    resoudreExercice = False
