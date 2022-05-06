class Carte :
    def __init__ (self, name, mana, description) :
        self._nom = name
        self._cout = mana
        self._description = description
        self._surTerrain = False
        self._dansMain = True
        self._dansDefausse = False

class Joueur :
    def __init__ (self, name, pv, manaFull, mana) :
        self._nom = name
        self._pv = pv
        self._manaTotal = manaFull
        self._manaActuel = mana
    def getNom1 (self) :
        return self._nom


class Main :
    def __init__ (self, listeCarte) :
        self._listeCarteMain = [listeCarte]
    def getListeCarte (self) :
        return self._listeCarteMain

class Defausse :
    def __init__ (self, listeDefause) :
        self._listeDefauseJoueur = listeDefause

class ZoneDeJeu :
    def __init__ (self, zoneDeJeuJoueur1, zoneDeJeuJoueur2 ) :
        self._ZoneDeJeuJoueur1 = zoneDeJeuJoueur1
        self._ZoneDeJeuJoueur2 = zoneDeJeuJoueur2

class Cristal(Carte) :
    def __init__ (self) :
        Carte.__init__ (self, "Cristal", 10, "Un cristal ancien et magique qui augmente votre Mana Total de +1")

class Creature(Carte) :
    def __init__ (self, dgts, name, mana, description, pv) :
        Carte.__init__ (self, "Creature", 10, "Test")
        self.degatsCreature = dgts
        self.creatureNom = name
        self.creatureMana = mana
        self.creatureDescription = description
        self.creaturePV = pv

class Blast(Carte) :
    def __init__ (self, dgtsBlast) :
        Carte.__init__ (self, "Blast", 10, "Une énorme explosion magique qui inflige des dégats équivalents au mana de ce Blast !")
        self.degatsBlast = dgtsBlast

#Main
print ("Bienvenue dans cette bataille de cartes magiques ! Vous pourrez jouer à 2, l'un contre l'autre en utilisant divers cartes afin de faire tomber les PV de l'adversaire à 0 !!")
Joueur1 = Joueur(input ("Mage 1, choissez votre nom : "), 20, 15, 15)
Joueur2 = Joueur(input ("Mage 2, choissez votre nom : "), 20, 15, 15)
tour = 0
victoire = False

print ("Joueur 1 = ", Joueur1._nom, " ! Et Joueur 2 = ", Joueur2._nom, " !")
print ("Vous allez jouer chacun votre tour en choisissant une carte parmis votre main que vous pourrez poser sur votre terrain ! Vous aurez 20 tours pour gagner, le vainqueur sera le joueur possedant le plus de point de vie !")

#while tour <20 or Joueur1._pv == 0 or Joueur2._pv == 0 :
print("C'est à ", Joueur1._nom, " de jouer !")
print("Vous avez ", Joueur1._manaActuel, " de Mana !" )
print ("Voici vos cartes disponibles : ")
carte1 = Creature(1, "Gobelin", 2, "Un gobelin de la tribu des montagnes. (2 MANA | 1 DGTS)", 2)
carte2 = Creature(2, "Troll", 3, "Un Troll solitaire des forêts. (3 MANA | 2 DGTS)", 3)
carte3 = Creature(3, "Roi des Loups", 4, "Le chef d'une immense meute de loups. (4 MANA | 3 DGTS)", 4)
carte4 = Creature(4, "Lechen", 5, "Un puissant esprit gardien de la forêt. (5 MANA | 4 DGTS)", 5)
carte5 = Creature(5, "Golem Ancien", 3, "Un ancien golem d'origine inconnue. (6 MANA | 5 DGTS)", 6)
carte6 = Cristal()
listeCarteJoueur1 = ["Gobelin", "Troll", "Roi des Loups", "Lechen", "Golem Ancien", "Cristal"]

print(listeCarteJoueur1)
choixCarteJoueur1 = input("Choisissez la carte à jouer : ")
if choixCarteJoueur1 in listeCarteJoueur1 :
    print(Joueur1._nom, "joue : ", choixCarteJoueur1)
    if choixCarteJoueur1 == "Gobelin" :
        choixCarteJoueur1 == carte1
        choixCarteJoueur1 = Creature(1, "Gobelin", 2, "Un gobelin de la tribu des montagnes. (2 MANA | 1 DGTS)", 2)
        carte1._surTerrain = True
        carte1._dansMain = False
        print(carte1.creatureDescription)
        Joueur1._manaActuel -= carte1.creatureMana
        print("Il vous reste ", Joueur1._manaActuel, " de Mana !" )

    if choixCarteJoueur1 == "Troll" :
        choixCarteJoueur1 == carte2
        choixCarteJoueur1 = Creature(2, "Troll", 3, "Un Troll solitaire des forêts. (3 MANA | 2 DGTS)", 3)
        carte2._surTerrain = True
        carte2._dansMain = False
        print(carte2.creatureDescription)
        Joueur1._manaActuel -= carte2.creatureMana
        print("Il vous reste ", Joueur1._manaActuel, " de Mana !" )

    if choixCarteJoueur1 == "Roi des Loups" :
        choixCarteJoueur1 == carte3
        choixCarteJoueur1 = Creature(3, "Roi des Loups", 4, "Le chef d'une immense meute de loups. (4 MANA | 3 DGTS)", 4)
        carte3._surTerrain = True
        carte3._dansMain = False
        print(carte3.creatureDescription)
        Joueur1._manaActuel -= carte3.creatureMana
        print("Il vous reste ", Joueur1._manaActuel, " de Mana !" )
    
    if choixCarteJoueur1 == "Lechen" :
        choixCarteJoueur1 == carte4
        choixCarteJoueur1 = Creature(4, "Lechen", 5, "Un puissant esprit gardien de la forêt. (5 MANA | 4 DGTS)", 5)
        carte4._surTerrain = True
        carte4._dansMain = False
        print(carte4.creatureDescription)
        Joueur1._manaActuel -= carte4.creatureMana
        print("Il vous reste ", Joueur1._manaActuel, " de Mana !" )

    if choixCarteJoueur1 == "Golem Ancien" :
        choixCarteJoueur1 == carte5
        choixCarteJoueur1 = Creature(5, "Golem Ancien", 3, "Un ancien golem d'origine inconnue. (6 MANA | 5 DGTS)", 6)
        carte5._surTerrain = True
        carte5._dansMain = False
        print(carte5.creatureDescription)
        Joueur1._manaActuel -= carte5.creatureMana
        print("Il vous reste ", Joueur1._manaActuel, " de Mana !" )

    if choixCarteJoueur1 == "Cristal" :
        choixCarteJoueur1 == carte6
        carte6._surTerrain = True
        carte6._dansMain = False
        print (carte6._description)
        Joueur1._manaActuel -= carte6._cout
        print("Il vous reste ", Joueur1._manaActuel, " de Mana !" )
        Joueur1._manaTotal +=1
        print("Vous avez joué un cristal ! +1 à votre mana totale. Mana totale =", Joueur1._manaTotal)

    #if choixCarteJoueur1 == "Blast" :
        #choixCarteJoueur1 == carte6
        #print(carte6._description)
        #Joueur1._manaActuel -= carte6._cout
        #print("Il vous reste ", Joueur1._manaActuel, " de Mana !" )
        #print("Vous avez joué un Blast ! Qui attaquer vous ?")

    print("C'est à ", Joueur2._nom, " de jouer !")
    print("Vous avez ", Joueur2._manaActuel, " de Mana !" )
    print ("Voici vos cartes disponibles : ")
    carte1j2 = Creature(1, "Poison-Tigre", 2, "Un gros poisson carnivore. (2 MANA | 1 DGTS)", 2)
    carte2j2 = Creature(2, "Vaseux", 3, "Une créature discrete des marais. (3 MANA | 2 DGTS)", 3)
    carte3j2 = Creature(3, "Chef du clan des Gators", 4, "Le chef du clan d'homme-crocodile. (4 MANA | 3 DGTS)", 4)
    carte4j2 = Creature(4, "Requin Géant", 5, "Un requin plus grand que la normale. (5 MANA | 4 DGTS)", 5)
    carte5j2 = Creature(5, "Leviathan", 3, "Une bête aquatique surpuissante. (6 MANA | 5 DGTS)", 6)
    carte6j2 = Cristal()
    listeCarteJoueur2 = ["Poison-Tigre", "Vaseux", "Chef du clan des Gators", "Requin Géant", "Leviathan", "Cristal"]

    print(listeCarteJoueur2)
    choixCarteJoueur2 = input("Choisissez la carte à jouer : ")
    if choixCarteJoueur2 in listeCarteJoueur2 :
        print(Joueur2._nom, "joue : ", choixCarteJoueur2)
        if choixCarteJoueur2 == "Poison-Tigre" :
            choixCarteJoueur2 == carte1j2
            choixCarteJoueur2 = Creature(1, "Poison-Tigre", 2, "Un gros poisson carnivore. (2 MANA | 1 DGTS)", 2)
            carte1j2._surTerrain = True
            carte1j2._dansMain = False
            print(carte1j2.creatureDescription)
            Joueur2._manaActuel -= carte1j2.creatureMana
            print("Il vous reste ", Joueur2._manaActuel, " de Mana !" )

        if choixCarteJoueur1 == "Vaseux" :
            choixCarteJoueur2 == carte2j2
            choixCarteJoueur2 = Creature(2, "Vaseux", 3, "Une créature discrete des marais. (3 MANA | 2 DGTS)", 3)
            carte2j2._surTerrain = True
            carte2j2._dansMain = False
            print(carte2j2.creatureDescription)
            Joueur2._manaActuel -= carte2j2.creatureMana
            print("Il vous reste ", Joueur2._manaActuel, " de Mana !" )

        if choixCarteJoueur2 == "Chef du clan des Gators" :
            choixCarteJoueur2 == carte3j2
            choixCarteJoueur2 = Creature(3, "Chef du clan des Gators", 4, "Le chef du clan d'homme-crocodile. (4 MANA | 3 DGTS)", 4)
            carte3j2._surTerrain = True
            carte3j2._dansMain = False
            print(carte3j2.creatureDescription)
            Joueur2._manaActuel -= carte3j2.creatureMana
            print("Il vous reste ", Joueur2._manaActuel, " de Mana !" )
        
        if choixCarteJoueur2 == "Requin Géant" :
            choixCarteJoueur2 == carte4j2
            choixCarteJoueur2 = Creature(4, "Requin Géant", 5, "Un requin plus grand que la normale. (5 MANA | 4 DGTS)", 5)
            carte4j2._surTerrain = True
            carte4j2._dansMain = False
            print(carte4j2.creatureDescription)
            Joueur2._manaActuel -= carte4j2.creatureMana
            print("Il vous reste ", Joueur2._manaActuel, " de Mana !" )

        if choixCarteJoueur2 == "Leviathan" :
            choixCarteJoueur2 == carte5j2
            choixCarteJoueur2 = Creature(5, "Leviathan", 3, "Une bête aquatique surpuissante. (6 MANA | 5 DGTS)", 6)
            carte5j2._surTerrain = True
            carte5j2._dansMain = False
            print(carte5j2.creatureDescription)
            Joueur2._manaActuel -= carte5j2.creatureMana
            print("Il vous reste ", Joueur2._manaActuel, " de Mana !" )

        if choixCarteJoueur2 == "Cristal" :
            choixCarteJoueur2 == carte6j2
            carte6j2._surTerrain = True
            carte6j2._dansMain = False
            print (carte6j2._description)
            Joueur2._manaActuel -= carte6j2._cout
            print("Il vous reste ", Joueur2._manaActuel, " de Mana !" )
            Joueur2._manaTotal +=1
            print("Vous avez joué un cristal ! +1 à votre mana totale. Mana totale =", Joueur2._manaTotal)

        #if choixCarteJoueur2 == "Blast" :
            #choixCarteJoueur2 == carte6j2
            #print(carte6j2._description)
            #Joueur2._manaActuel -= carte6j2._cout
            #print("Il vous reste ", Joueur2._manaActuel, " de Mana !" )
            #print("Vous avez joué un Blast ! Qui attaquer vous ?")

    print ("Phase d'attaque !")
    choixCibleJoueur1 = input("Choisissez votre cible Joueur1 : Mage ou Mob ? ")
    if choixCibleJoueur1 == "Mage" :
        if choixCarteJoueur1 == carte1 :
            Joueur2._pv -= carte1.degatsCreature
            print("Les PV du Mage adverse sont à ", Joueur2._pv)

        if choixCarteJoueur1 == carte2 :
            Joueur2._pv -= carte2.degatsCreature
            print("Les PV du Mage adverse sont à ", Joueur2._pv)

        if choixCarteJoueur1 == carte3 :
            Joueur2._pv -= carte3.degatsCreature
            print("Les PV du Mage adverse sont à ", Joueur2._pv)

        if choixCarteJoueur1 == carte3 :
            Joueur2._pv -= carte3.degatsCreature
            print("Les PV du Mage adverse sont à ", Joueur2._pv)

        if choixCarteJoueur1 == carte4 :
            Joueur2._pv -= carte4.degatsCreature
            print("Les PV du Mage adverse sont à ", Joueur2._pv)
        
        if choixCarteJoueur1 == carte5 :
            Joueur2._pv -= carte5.degatsCreature
            print("Les PV du Mage adverse sont à ", Joueur2._pv)

        if choixCarteJoueur1 == carte6 :
            print("Vous ne pouvez attaquer sans Mobs !")

    if choixCibleJoueur1 == "Mob" :
        choixCarteJoueur2.creaturePV -= choixCarteJoueur1.degatsCreature
        choixCarteJoueur1.creaturePV -= choixCarteJoueur2.degatsCreature
        print("Votre créature a attaqué celle de votre adversaire")
        if choixCarteJoueur2.creaturePV == 0 :
            choixCarteJoueur2._surTerrain = False
            choixCarteJoueur2._dansDefausse =  True
            print("Votre créature à vaincu celle de votre adversaire !")

        if choixCarteJoueur1.creaturePV == 0 :
            choixCarteJoueur1._surTerrain = False
            choixCarteJoueur1._dansDefausse = True
            print("L'adversaire à vaincu votre créature !")

        if choixCarteJoueur1.creaturePV == 0 :
            choixCarteJoueur1._surTerrain = False
            choixCarteJoueur2._dansDefausse = True

    if choixCarteJoueur1._dansDefausse == True :
        listeCarteJoueur1.pop(choixCarteJoueur1)

    if choixCarteJoueur2._dansDefausse == True :
        listeCarteJoueur2.pop(choixCarteJoueur2)

    if Joueur1._pv == 0 :
        print (Joueur2._nom, "a gagné !!")

    if Joueur2._pv == 0 :
        print (Joueur1._nom, "a gagné !!")

    tour = tour +1
    Joueur1._manaActuel += 2
    Joueur2._manaActuel += 2

    print("Tour suivant")