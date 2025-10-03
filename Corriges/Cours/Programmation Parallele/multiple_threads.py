# Threads qui gaspillent des cycles CPU

# Imports
import os
import threading

# Une simple fonction qui ne fait que gaspiller des cycles CPU.
def gaspillageCPU():
    while True:
        pass

if __name__ == "__main__":
    # Affichage d'information sur le processus et les threads.
    print(f"\nIdentifiant du processus : {os.getpid()}")
    print(f"Nombre de threads : {threading.active_count()}")

    for thread in threading.enumerate():
        print(thread)

    print("\nDémarrage du gaspillage CPU...")
    
    # Création de 4 threads.
    for i in range(4):
        threading.Thread(target = gaspillageCPU).start()

    # Affichage d'information sur le processus et les threads.
    print(f"\nIdentifiant du processus : {os.getpid()}")
    print(f"Nombre de threads : {threading.active_count()}")

    for thread in threading.enumerate():
        print(thread)

    # A cause du GIL un seul thread s'excute à un moment donnée.
    # En regardant la mémoire et la charge du processeur on s'apercoit
    # que la charge du processeur est moins élevée qu'avec le multiprocessing.
    