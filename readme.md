Projet: Space Invaders  
Auteurs: MICHALOPOULOS Zaphirios et OUENADIO Alexandre


Lien du dépot Github : https://github.com/AlexUnise/Space-Invaders

Commandes du jeu:
Q: Déplacement à gauche
D: Déplacement à droite
Espace: Tir

Règles du jeu:
- Vous perdez dès que vous perdez vos 3 vies
- Vous perdez si vous ennemis atteignent vos murs de protections
- Vous gagnez si vous tuez tous les ennemis (l'ennemi bonus n'est pas necessaire)

Comment lancer le jeu ?:
- Lancer le programme main.py
- Appuyer sur le bouton New Game lance la partie


La pile est utiliée pour la construction des murs de protection(Class Protection/self.__listProtections)
La file est utilisée pour relancer un partie, afin de suprimmer les "after" toujours valables dans le programme (Class Space_Invaders / pour la variable self.__afterFunctions / dans def start_game/ le premier if )


