# Deux acheteurs ajoutant des articles à un bloc-notes partagé
import threading

nbLivres = 0
mutex = threading.Lock()

def acheteur():
    global nbLivres

    # Ne pas mettre une grande valeur à cause du print qui est très lent.
    for _ in range(10_000):
        print(threading.current_thread().getName(), "Refléchit ...")
        # Section de code pouvant causer un data_race à prtéger.
        mutex.acquire()
        nbLivres += 1
        mutex.release()

if __name__ == "__main__":
    barron = threading.Thread(target = acheteur)
    olivia = threading.Thread(target = acheteur)
    barron.start()
    olivia.start()
    barron.join()
    olivia.join()
    print(f"Nous devons acheter {nbLivres} livres.")