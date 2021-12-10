from fltk import *

cree_fenetre(400, 400)

ax = 10
ay = 10
bx = 100
by = 200
rectangle(ax, ay, bx, by, tag='allu1')


while True:
    ev = donne_ev()
    tev = type_ev(ev)

    def efface_allu(allu):
        if tev == "ClicGauche":
            print('Clic gauche au point', (abscisse(ev), ordonnee(ev)))
            if (ax < abscisse(ev) < bx) and (ay < ordonnee(ev) < by):
                efface(allu)
        else:
            pass
        mise_a_jour()
    efface_allu('allu1')
    if tev == 'Quitte':
        break

ferme_fenetre()    


    
