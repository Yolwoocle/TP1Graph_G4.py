#!/usr/bin/env python
# vim: set sw=4 sts=4 et fdm=marker:
# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ Nom: Carlisi Nolan && BERNARD Léo, En TG 04 ┃
# ┃ Creation: 18/03/2022 11:35:24               ┃
# ┃ Mise a jour: 26/03/2022                     ┃
# ┃ Fichier: TP1BisGraph_G4.py                  ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

def graph_to_matrice(G):
    matrice = [[0] * len(G) for _ in range(len(G.keys()))]
    for k, valeurs in G.items():
        for valeur in valeurs:
            matrice[ord(k) - 97][ord(valeur) - 97] = 1

    return matrice


def draw_matrice(matrice):
    print(" ", " ".join([chr(i + 97) for i in range(len(matrice))]), end="")
    for ind, i in enumerate(matrice):
        print(f"\n{chr(ind + 97)} ", end="")
        for j in i:
            print(f"{j} ", end="")
    return


def nombre_sommets(matrice):
    """Renvoie le nombre de sommets d'un graphe"""
    return len(matrice)


def voisins(matrice, ind):
    """Renvoie une liste des voisins d'un sommet"""
    return matrice[ind]


def degre(matrice, ind):
    """Renvoie le degré d'un sommet, autrement dit son nombre de voisins"""
    voisin = 0
    for i in matrice[ind]:
        if i == 1:
            voisin += 1
    return voisin


def max_degre_sommet(matrice):
    """Renvoie le sommet ayant le plus haut degré"""
    max_degre = 0
    for i in range(len(matrice)):
        if degre(matrice, i) > max_degre:
            max_degre = degre(matrice, i)
            max_degre_sommet = i
    return max_degre_sommet


def nombre_aretes(matrice):
    """Renvoie le nombre d'arêtes dans le graphe"""
    nb_aretes = 0
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if matrice[i][j] == 1:
                nb_aretes += 1
    return nb_aretes // 2


def main():
    G = dict()
    G['a'] = ['b', 'c']
    G['b'] = ['a', 'd', 'e']
    G['c'] = ['a', 'd']
    G['d'] = ['b', 'c', 'e']
    G['e'] = ['b', 'd', 'f', 'g']
    G['f'] = ['e', 'g']
    G['g'] = ['e', 'f', 'h']
    G['h'] = ['g']
    matrice = graph_to_matrice(G)

    print("matrice[4]:  ", matrice[4])
    print("")
    print("*** Tests for les fonctions ***")
    print("nombre_sommets(G):  ", nombre_sommets(matrice))
    print("voisins(G, 'a'):    ", voisins(matrice, 0))
    print("degre(G, 'b'):      ", degre(matrice, 1))
    print("max_degre_sommet(G):", max_degre_sommet(matrice))
    print("nombre_aretes(G):   ", nombre_aretes(matrice))

    print("*** Matrice G ***")
    draw_matrice(matrice)

    print("\n" * 3)

    X = dict()
    X['a'] = ['b', 'f']
    X['b'] = ['a', 'c', 'd', 'g']
    X['c'] = ['b', 'e']
    X['d'] = ['b', 'i']
    X['e'] = ['c', 'i']
    X['f'] = ['a', 'g', 'h']
    X['g'] = ['b', 'i', 'f']
    X['h'] = ['f', 'i']
    X['i'] = ['d', 'e', 'g', 'h']

    matrice = graph_to_matrice(X)

    print("matrice[4]:  ", matrice[4])
    print("")
    print("*** Tests for les fonctions ***")
    print("nombre_sommets(G):  ", nombre_sommets(matrice))
    print("voisins(G, 'a'):    ", voisins(matrice, 0))
    print("degre(G, 'b'):      ", degre(matrice, 1))
    print("max_degre_sommet(G):", max_degre_sommet(matrice))
    print("nombre_aretes(G):   ", nombre_aretes(matrice))

    print("*** Matrice X ***")
    draw_matrice(matrice)


if __name__ == "__main__":
    main()
