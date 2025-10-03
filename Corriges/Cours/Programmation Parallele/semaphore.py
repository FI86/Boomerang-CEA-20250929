# Connecter des téléphones portables à un chargeur.

import random
import threading
import time

# Nombre limite de charge simultanée.
charger = threading.Semaphore(4)

def mobile():
    # Nom du thread.
    # Avant la version 3.10
    # nom = threading.current_thread().getName()
    # Depuis la version 3.10
    nom = threading.current_thread().name

    with charger:
        print(f"{nom} est en charge ...")
        # Temps de charge aléatoire entre 1 et 2s.
        time.sleep(random.uniform(1, 2))
        print(f"{nom} est chargé !")

if __name__ == "__main__":
    for tel in range(10):
        threading.Thread(target=mobile, name=f"Téléphone - {tel}").start()