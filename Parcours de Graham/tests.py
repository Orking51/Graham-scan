import mon_projet_docs.main_working as m

def test_listformat():
    """
    Liste de points utilisée pour le test: [(0,0),(2,5),(9,3)]
    Résultat attendu: ([0,2,9], [0,5,3])
    """
    if m.listformat([(0,0),(2,5),(9,3)]) == ([0,2,9], [0,5,3]):
        print("listformat: ok")
    else:
        print('Error with function "listformat"')

def test_affichage():
    """
    Liste des points à afficher utilisé pour le test: [(0,0),(2,5),(9,3),(10,10)]
    Liste des points à relier utilisée pour le test: [(0,0),(2,5),(9,3)]
    Point pivot utilisé pour le test: ((0,0), 0) 
    Résultat attentdu: None
    Devrait ouvrir une fenêtre Matplotlib avec les points (0,0),(2,5),(9,3) reliés, le point (0,0) en cyan et le point (10,10) non relié
    """
    if m.affichage([(0,0),(2,5),(9,3),(10,10)], [(0,0),(2,5),(9,3)], ((0,0), 0)) == None:
        print("affichage: ok")
    else:
        print("Error with function: affichage")

def test_test_if_out():
    """
    Liste des points utilisé pour le test: [(0,0),(2,5),(9,3)] puis [(0,0),(2,5),(3,8)]
    Résultat attendu: False puis True
    """
    if m.test_if_out((0,0),(2,5),(9,3)) == False:
        if m.test_if_out((0,0),(2,5),(3,8)) == True:
            print("test_if_out: ok")
        else:
            print("Error with function: test_if_out (2nd list)")
    else:
        print("Error with function: test_if_out (1st list)")

def test_sort_angles():
    """
    Point pivot utilisé pour le test: ((0,0), 2)
    Liste de points utilisée pour le test: [(2,5),(9,3),(0,0),(3,8)]
    Résultat attendu: [(0, 0), (9, 3), (2, 5), (3, 8)]
    """
    if m.sort_angles(((0,0), 2),[(2,5),(9,3),(0,0),(3,8)]) == [(0, 0), (9, 3), (2, 5), (3, 8)]:
        print("sort_angles: ok")
    else:
        print("Error with function: sort_angles")

def test_find_pivot():
    """
    Liste de points utilisés por le test: [(2,5),(9,3),(0,0),(3,8)]
    Résultat attendu: ((0,0),2)
    """
    if m.find_pivot([(2,5),(9,3),(0,0),(3,8)]) == ((0,0), 2):
        print("find_pivot: ok")

def test_enlever_doublons():
    """
    Liste de points utilisée pour le test: [(2,5),(3,8),(9,3),(0,0),(3,8)]
    Résultat attendu: [(3, 8), (2, 5), (9, 3), (0, 0)]
    """
    if m.enlever_doublons([(2,5),(3,8),(9,3),(0,0),(3,8)]) == [(3, 8), (2, 5), (9, 3), (0, 0)]:
        print("enlever_doublons: ok")
    else: print("Error with function: enlever_doublons")

def test_gen_points():
    """
    Paramètres utilisés pour le test:
        n: 10
        Omin: 0
        Omax: 20
        Amin: 0
        Amax: 20
    Devrait renvoyer une liste de coordonnées de 10 points compris en 0 et 20 d'abscisse et d'ordonnée
    """
    if len(m.gen_points(10,0,20,0,20)) == 10 and type(m.gen_points(10,0,20,0,20)) == list:
        print(f"Liste de points retournée par gen_points: {m.gen_points(10,0,20,0,20)}")
        print("gen_points: ok")
    else:
        print("Error with function: gen_points")

def test_saisie():
    """
    Paramètres utilisés pour le test:
        question: "nombre_de_points"
        saisie: "2"
        max: None
    Résultat attendu: 2
    """
    if m.saisie("nombre_de_points", "2", None) == 2:
        print("saisie: ok")
    else:
        print("Error with function: saisie")

if __name__ == "__main__":
    test_listformat()
    test_affichage()
    test_test_if_out()
    test_sort_angles()
    test_find_pivot()
    test_enlever_doublons()
    test_gen_points()
    test_saisie()