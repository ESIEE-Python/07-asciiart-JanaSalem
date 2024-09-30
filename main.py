"""Voici le Code de Salem Jana"""
import sys


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne
      de caractères passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    compteur = 1
    count = []

    for i in range(len(s)-1): # on met -1 pour pas causer un index hors limites

        if s[i] == s[i+1]:
            compteur = compteur + 1

        else:
            count.append((s[i], compteur))
            compteur = 1

    count.append((s[-1], compteur))  # ne pas oublier d'ajouter le dernier caractère

    return count



sys.setrecursionlimit(1200)  # Car erreru de recursion

def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de 
    caractères passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    if len(s) == 0:  # Cas de base
        return []

    compteur = 1
    while compteur < len(s) and s[compteur] == s[0]:
        compteur += 1
    tuplle = (s[0], compteur) # Créer le tuple pour le premier caractère

    return [tuplle] + artcode_r(s[compteur:])  # Appel récursif

#### Fonction principale


def main():
    """La Fonction main
    """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
