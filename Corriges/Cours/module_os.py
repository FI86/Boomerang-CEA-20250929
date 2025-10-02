# Fichier d'exemples avec le module os

# Imports
import os
from os import path

import datetime
import time
import platform

def main():
    chemin = os.path.dirname(__file__)
    nomFichier = "osFichierTest.txt"

    # Afficher le chemin courant, le nom de l'OS
    print(chemin)
    print(os.getcwd())
    print(os.name)
    
    print("variables d'environnements :", list(os.environ.keys()))
    print("dossier courant :", os.curdir, "dossier parent :", os.pardir)
    # sans repr de os.linesep cela faut un saut de ligne sans voir la representation de celui-ci
    print("separateur de dossier :", os.sep, "separateur de chemin :", os.pathsep, "separateur de ligne :", repr(os.linesep))
    print("systeme :", platform.system())
    print("realease :", platform.release())
    version = platform.version()
    print("version :", version)
    build = int(version.split(".")[-1]) if version else 0
    print("build :", build)

    # Vérification de l'existence d'un élément et de son type
    print(f"L'element existe : {str(path.exists(path.join(chemin, nomFichier)))}")
    print(f"L'element est un fichier : {str(path.isfile(path.join(chemin, nomFichier)))}")
    print(f"L'element est un dossier : {str(path.isdir(path.join(chemin, nomFichier)))}")

    # Manipuler les informations sur le chemin du fichier avec file paths
    print(f"Le chemin du fichier : {str(path.realpath(path.join(chemin, nomFichier)))}")
    print(f"Le chemin du fichier et sa designation : {str(path.split(path.realpath(path.join(chemin, nomFichier))))}")

    # Obtenir la date de modification du fichier
    print(f"Date de modification du fichier : {time.ctime(path.getmtime(path.join(chemin, nomFichier)))}")
    print(f"Date de modification du fichier : {datetime.datetime.fromtimestamp(path.getmtime(path.join(chemin, nomFichier)))}")

    # Caclucler le temps écoulé depuis la dernière modification
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime(path.join(chemin, nomFichier)))
    print(f"Il s'est passé {str(td)} depuis la dernière modification")
    print(f"Ou, {str(td.total_seconds())} secondes")

if __name__ == "__main__":
    main()