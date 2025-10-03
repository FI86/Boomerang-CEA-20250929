# Processus qui gaspillent des cycles CPU
import os
import threading
import multiprocessing as mp

# Une simple fonction qui ne fait que gaspiller des cycles CPU.
def gaspillageCPU():
    while True:
        pass

if __name__ == "__main__":
    # Affichage d'information sur le processus.
    print(f"\nIdentifiant du processus : {os.getpid()}")
    print(f"Nombre de threads : {threading.active_count()}")

    for thread in threading.enumerate():
        print(thread)

    print("\nDémarrage du gaspillage CPU...")

    # Création de plusieurs processus.
    for i in range(4):
        mp.Process(target = gaspillageCPU).start()

    # Affichage d'information sur le processus.
    print(f"\nIdentifiant du processus : {os.getpid()}")
    print(f"Nombre de threads : {threading.active_count()}")

    for thread in threading.enumerate():
        print(thread)

    # En regardant la mémoire et la charge du processeur on s'apercoit
    # que la charge du processeur est plus élevée qu'avec le multithreading.