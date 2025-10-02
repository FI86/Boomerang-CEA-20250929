"""
Module d'exemple avec DocTests.
Pour exécuter :
    python -m doctest -v doctests.py
"""
import doctest

def carre(x):
    """
    Retourne le carré de x.

    >>> carre(3)
    9
    >>> carre(-2)
    4
    """
    return x * x


def factorielle(n):
    """
    Calcule la factorielle de n.

    >>> factorielle(0)
    1
    >>> factorielle(5)
    120
    >>> factorielle(3)
    6
    >>> factorielle(-1)
    Traceback (most recent call last):
        ...
    ValueError: La factorielle n'est pas définie pour les entiers négatifs.
    """
    if n < 0:
        raise ValueError("La factorielle n'est pas définie pour les entiers négatifs.")
    if n == 0:
        return 1
    return n * factorielle(n - 1)


def est_pair(n):
    """
    Retourne True si n est pair, False sinon.

    >>> est_pair(4)
    True
    >>> est_pair(5)
    False
    >>> est_pair(-2)
    True
    """
    return n % 2 == 0


if __name__ == "__main__":
    doctest.testmod(verbose=True)
