#!/usr/bin/env python
# vim: set sw=4 sts=4 et fdm=marker:
# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ Nom: Carlisi Nolan && BERNARD Léo, En TG 04 ┃
# ┃ Creation: 18/03/2022 12:27:34               ┃
# ┃ Mise a jour: 26/03/2022                     ┃
# ┃ Fichier: TP1Graph_G4.py                     ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

def nombre_sommets(G):
    """Renvoie le nombre de sommets d'un graphe"""
    return len(G.keys())

def voisins(G, val):
    """Renvoie une liste des voisins d'un sommet"""
    return G[val]

def degre(G, val):
    """Renvoie le degré d'un sommet, autrement dit son nombre de voisins""" 
    voisins = 0
    for i in G[val]:
        if i != val:
            voisins += 1
    return voisins

def max_degre_sommet(G):
    """Renvoie le sommet ayant le plus haut degré"""
    assert len(G.keys()) > 0, "Graphe vide"
    
    max_sommet = ""
    max_degre = 0
    for sommet in G.keys():
        deg = degre(G, sommet)
        if deg > max_degre:
            max_sommet = sommet
            max_degre = deg
    return max_sommet

def nombre_aretes(G):
    """Renvoie le nombre d'arêtes dans le graphe"""
    sum_deg = 0
    for k,v in G.items():
        sum_deg += degre(G,k)
    return sum_deg // 2

def main(): 
    G = dict()
    G['a'] = ['b','c']
    G['b'] = ['a','d','e']
    G['c'] = ['a','d']
    G['d'] = ['b','c','e']
    G['e'] = ['b','d','f','g']
    G['f'] = ['e','g']
    G['g'] = ['e','f','h']
    G['h'] = ['g']

    print("")
    print("*** Graphe G ***")
    print("G.keys:  ", list(G.keys()))
    print("G.values:", list(G.values()))
    print("len(G):  ", len(G))
    for k,v in G.items():
        print(f'{k}: {v}')
    print("G['e']:  ", G['e'])
    print("")
    print("*** Tests for les fonctions ***")
    print("nombre_sommets(G):  ", nombre_sommets(G))
    print("voisins(G, 'a'):    ", voisins(G, 'a'))
    print("degre(G, 'b'):      ", degre(G, 'b'))
    print("max_degre_sommet(G):", max_degre_sommet(G))
    print("nombre_aretes(G):   ", nombre_aretes(G))

    print("\n"*3)
    
    X = dict()
    X['a'] = ['b','f']
    X['b'] = ['a','c','d','g']
    X['c'] = ['b','e']
    X['d'] = ['b','i']
    X['e'] = ['c','i']
    X['f'] = ['a','g','h']
    X['g'] = ['b','i','f']
    X['h'] = ['f','i']
    X['i'] = ['d','e','g','h']

    print("")
    print("*** Graphe X ***")
    print("X.keys:  ", list(X.keys()))
    print("X.values:", list(X.values()))
    print("len(X):  ", len(X))
    for k,v in X.items():
        print(f'{k}: {v}')
    print("")
    print("*** Tests for les fonctions ***")
    print("nombre_sommets(X):  ", nombre_sommets(X))
    print("voisins(X, 'a'):    ", voisins(X, 'a'))
    print("degre(X, 'b'):      ", degre(X, 'b'))
    print("max_degre_sommet(X):", max_degre_sommet(X))
    print("nombre_aretes(X):   ", nombre_aretes(X))

if __name__ == "__main__":
    main()

