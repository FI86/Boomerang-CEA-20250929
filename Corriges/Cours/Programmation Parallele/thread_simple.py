# Thread simple

import threading
import time

def ma_fonction():
    print(f"Début du thread : {threading.current_thread().name}")
    time.sleep(2)
    print(f"Fin du thread : {threading.current_thread().name}")

# Creer un thread avec un nom personnalise
t = threading.Thread(target=ma_fonction, name="MonThread")

# Demarrer le thread
t.start()

# Attendre la fin du thread
t.join()

print("Thread terminé.")
