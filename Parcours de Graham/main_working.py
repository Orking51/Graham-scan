import random as rd
import math
import matplotlib.pyplot as plt

def listformat(tab: list) -> tuple:
    """
    Change l'ordre des coordonnées de points afin de les utiliser avec Matplotlib :
    - Prend en argument tab, liste contenant des tuples de coordonnées (format x, y)
    - Retourne un tuple de deux listes, avec formatedx contenant toutes les valeurs x des coordonnées des points et formatedy contenant toutes les valeurs y des coordonnées des points.
    """

    formatedx = []
    formatedy = []
    for e in tab:
        formatedx.append(e[0])
        formatedy.append(e[1])
    return formatedx, formatedy

def affichage(tab: list, coordinates: list, pivot: tuple) -> None: 
    """
    Affiche le résultat du parcours de Graham dans le nuage de points :
    - Prend en argument tab, liste originelle du nuage de points ; coordinates, coordonnées des points de l'enveloppe convexe ; pivot, le point pivot utilisé pour l'algorithme de Graham.
    - Ne retourne rien, mais affiche le résultat dans une fenêtre.
    """

    #INITIALISATION DU REPERE
    fig, ax = plt.subplots()



    # AFFICHAGE DES POINTS
    x, y = listformat(tab)
    ax.plot(x, y, "o", c="b")



    # AFFICHAGE DU POINT PIVOT
    ax.plot(pivot[0][0], pivot[0][1], "o", c="c", lw=5)



    # CONSTRUCTION DU POLYGONE
    for i in range(len(coordinates)):
        line = [coordinates[i], coordinates[(i+1)%(len(coordinates))]]
        x, y = listformat(line)
        ax.plot(x, y, c="r")

    plt.show()

    return None

def test_if_out(pointS1: tuple, pointS2: tuple, pointS3: tuple) -> bool:
    """
    Cherche si on peut tracer une droite entre les points S1 et S3 telle que le point S2 soit à gauche de cette droite :
    - Dans le compte rendu, il est expliqué ce que sont les points S1, S2 et S3.
    - Prend en entrée les coordonnées des points S1, S2 et S3 respectivement nommés : pointS1, pointS2 et pointS3.
    - On regarde le signe du produit vectoriel. Dans le cas où la fonction retourne True, le point S2 est correctement placé. Sinon, si le signe est négatif, la fonction retourne False, le point S2 est mal placé.
    """
    produit_vectoriel = (pointS2[0] - pointS1[0]) * (pointS3[1] - pointS1[1]) - (pointS3[0] - pointS1[0]) * (pointS2[1] - pointS1[1])
    if produit_vectoriel < 0:
        return False
    else:
        return True 

def sort_angles(pivot: tuple, tab: list) -> list: 
    """
    Trie les points de la liste tab par angle croissant par rapport au pivot :
    - Prend en entrée les coordonnées du pivot et un tableau de coordonnées de points.
    - Retourne la liste de points triée.
    """
    def calc_angle(point):
        return math.atan2(point[1]-pivot[0][1],point[0]-pivot[0][0])
    tab=sorted(tab, key=lambda x: x[0])
    list_coords = sorted(tab,key=calc_angle)
    return list_coords

def find_pivot(tab: list) -> tuple:
    """
    Cherche le point pivot :
    - Prend en argument tab, tableau contenant les coordonnées des points composant un nuage de points.
    - Retourne sous forme de tuple -> le tuple des coordonnées du point pivot et son index dans la liste originale.
    """
    current = tab[0][1], tab[0], 0
    for i in range(len(tab)):
        if not i == 0:
            if tab[i][1] == current[0]:
                if tab[i][0] < current[1][0]:
                    current = tab[i][1], tab[i], i
            else:
                if tab[i][1] < current[0]:
                    current = tab[i][1], tab[i], i
    return current[1], current[2]

def enlever_doublons(Liste: list) -> list:
    """
    Enlève les doublons :
    - Prend en argument une liste de coordonnées soit générée par gen_points() ou entrée à la main par Saisie_manuelle().
    - Retourne la liste sans les doublons.
    
    """
    return list(set(Liste))

def gen_points(n: int, Omin: int, Omax: int, Amin: int, Amax: int) -> list:
    """
    Fonction qui génère un nombre n aléatoirement de points compris entre les abscisses Amin et Amax et les ordonnées Omin et Omax.
    Retourne une liste de coordonnées rangées aléatoirement des n points.
    """
    list = []
    for i in range(n):
        list.append((rd.randint(Amin,Amax),rd.randint(Omin,Omax)))
    list = enlever_doublons(list)
    return list 

def saisie_manuelle() -> list:
    """
    Fonction qui prend aucun argument et qui retourne la saisie des coordonnées entrée par l'utilisateur dans une liste.
    """
    loop = True
    ListeString = input("entrer votre liste de coordonné comme ceci: (a,b),(c,d),(e,f)")
    while loop:
        try: 
            elements = ListeString.replace("(","").replace(")","").split(",") #Permet de convertir la liste saisie en tuple, et donc en données acceptables pour le programme.
            Liste=[]
            for i in range(0, len(elements), 2):
                Liste.append((int(elements[i]), int(elements[i + 1])))
            Liste = enlever_doublons(Liste)
            loop = False
        except:
            ListeString = input("Veuillez respecter la nomenclature et entrer uniquement des entiers de la manière suivante : (a,b),(c,d),(e,f)")
    return Liste

def saisie(question: str, saisie: str, max) -> list:
    """
    Fonction qui prend pour arguments un input utilisateur, une question (de type str) préalablement définie, et une variable max (qui permet d'éviter que l'ordonnée minimale soit supérieure à l'ordonnée maximale, et de même pour les abscisses).
    La fonction renvoie la saisie de l'utilisateur après avoir vérifié que les données entrées sont conformes.
    """
    loop=True
    while loop:

        if question=="nombre_de_points": #Le nombre de points doit être entier, positif et strictement supérieur à 2.
            try: 
                saisie = int(saisie)
                verif = saisie > 1
                if verif: loop=False
                else: saisie=input("Veuillez saisir un nombre entier positif strictement supperieur à 1. Réessayez:\n>>> ")
            except:
                saisie=input("Veuillez saisir un nombre entier positif strictement supperieur à 1. Réessayez:\n>>> ")

        if question=="ordonnee_max": #L'ordonnée maximale doit être un nombre entier.
            try:
                saisie = int(saisie)
                loop=False
            except:
                saisie=input("Veuillez saisir un nombre entier. Réessayez:\n>>> ")

        if question=="ordonnee_min": #L'ordonnée minimale doit être un nombre entier inférieur à l'ordonnée maximale.
            try:
                saisie = int(saisie)
                verif = saisie < max
                if verif: loop=False
                else: saisie=input("Veuillez entrer un nombre entier strictement inferieur à l'ordonnée max. Réessayez:\n>>> ")
            except:
                saisie=input("Veuillez entrer un nombre entier strictement inferieur à l'ordonnée max. Réessayez:\n>>> ")

        if question=="abscisse_max": #L'abscisse max doit être un nombre entier'
            try:
                saisie = int(saisie)
                loop=False
            except:
                saisie=input("Veuillez entrer un nombre entier. Réessayez:\n>>> ")

        if question=="abscisse_min": #L'abscisse minimale doit être un nombre entier strictement inférieur à l'abscisse maximale.
            try:
                saisie = int(saisie)
                verif = saisie < max
                if verif: loop=False
                else: saisie=input("Veuillez entrer un nombre entier strictement inferieur à l'ordonnée max. Réessayez:\n>>> ")
            except:
                saisie=input("Veuillez entrer un nombre entier strictement inferieur à l'abscisse max. Réessayez:\n>>> ")

        
    return saisie

def choix_de_generation_des_points() -> list:
    """
    Fonction qui prend aucun argument et qui retourne une liste de coordonnées conformément aux préférences de l'utilisateur.
    """
    print("Bienvenue dans notre algorithme")
    genere_aleatoire = input("Voulez-vous que l'ordinateur génère des points aléatoires? (o/n)\n>>> ")
    if genere_aleatoire == 'o':
                
        nombre_de_points = saisie("nombre_de_points", input("Quel est le nombre de points que vous voulez générer?\n>>> "), None)
        ordonnee_max = saisie("ordonnee_max", input("Quel sera l'ordonné max donné aux points?\n>>> "), None)
        ordonnee_min = saisie("ordonnee_min", input("Quel sera l'ordonné min donné aux points?\n>>> "), ordonnee_max)
        abscisse_max = saisie("abscisse_max", input("Quelle sera l'abscisse max donnée aux points?\n>>> "), None)
        abscisse_min = saisie("abscisse_min", input("Quelle sera l'abscisse min donnée aux points?\n>>> "), abscisse_max)
                
        ListeDePoints = gen_points(nombre_de_points, ordonnee_min, ordonnee_max, abscisse_min, abscisse_max)
        
    elif genere_aleatoire == 'n': ListeDePoints = saisie_manuelle()

    else: print("Veuillez saisir soit o, soit n\n>>>")  

    return ListeDePoints

def parcours_de_Graham():
    """
    Fonction principale qui permet de lier les autres fonctions ensemble et de créer la liste des points à relier.
    La fonction finit par envoyer la liste des points à relier à la fonction affichage.
    """
    ListeDePoints = choix_de_generation_des_points()
    pivot = find_pivot(ListeDePoints)

    element = ListeDePoints.pop(pivot[1])
    ListeDePoints = sort_angles(pivot, ListeDePoints)
    ListeDePoints.insert(0, element)
    
    ListeGraham = [ListeDePoints[0],ListeDePoints[1]]
    for i in range(2,len(ListeDePoints)):   #Cœur de l'algorithme de Graham : consultez le rapport ou la page Wikipédia pour en comprendre le fonctionnement
        while (len(ListeGraham)>=2) and test_if_out(ListeGraham[-2],ListeDePoints[i],ListeGraham[-1]) : 
            ListeGraham.pop(-1)
        ListeGraham.append(ListeDePoints[i])

    affichage( ListeDePoints, ListeGraham, pivot)

if __name__ == "__main__": 
    parcours_de_Graham()
