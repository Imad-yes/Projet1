from fltk import *

cree_fenetre(400, 400)

ax = 10
ay = 10
bx = 100
by = 200
rect1 = (rectangle(ax, ay, bx, by))


while True:
    ev = donne_ev()
    tev = type_ev(ev)

    if tev == "ClicGauche":
        print("Clic gauche au point", (abscisse(ev), ordonnee(ev)))
        if (ax < abscisse(ev) < bx) and (ay < ordonnee(ev) < by) :
            efface (rect1) 
    elif tev == 'Quiite':
        break
    else:  
        pass

    mise_a_jour()

ferme_fenetre()
