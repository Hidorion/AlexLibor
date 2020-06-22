#Importing a module to to use a randomiser
import random
#Importing a module to control caracters
import re
#Replay Part1
Rejouer = "Oui"
while Rejouer == "Oui" :
    print()
    print("BIENVENUE A LA WILD ROLLING DICE SCHOOL !!!")
    print()
    print(" ._____________. ")
    print(" |             | ")
    print(" | \         / | ")
    print(" |  \   ^   /  | ")
    print(" |   \ / \ /   | ")
    print(" |    V   V    | ")
    print(" |_____________| ")
    print()
#Instructions
    print("Deux joueurs lancent chacun 2 dés.")
    print("Il est possible de choisir la face de son set de dès.")
    print("En cas d'égalité', les dés sont relancés jusqu'à ce qu'il y ait un vainqueur.")
    print("Un vainqueur est désigné.")
    print()
    Nbdee = 2
#Chosing the number of players (cancelled)
#Users give their names and make sure it's not something else than letters   
    Player1 = str(input("Joueur 1, quel est ton nom ? "))
    while not re.match("^[A-Za-z]*$", Player1) or Player1 == "":
       Player1 = str(input("Joueur 1, quel est ton nom ? (Utilisez juste des lettres s.v.p.) "))
    print("Bonjour " + str(Player1))
    Player2 = str(input("Joueur 2, quel est ton nom ? "))
    while Player2 == "" or not re.match("^[A-Za-z]*$", Player2):
        Player2 = str(input("Joueur 2, quel est ton nom ? (Utilisez juste des lettres s.v.p.) "))
#no matching names.    
    if Player1 == Player2:
        Player2 = Player2 + " n°2"
    print("Bonjour " + str(Player2))
    NbFace = int(input("Combien de faces auront vos dés ? 4, 6, 8, 10, 12, 20 ou 100 ? "))
    NbFacevalide = [4, 6, 8, 10, 12, 20, 100]
    while NbFace not in NbFacevalide:        
        NbFace = int(input("Les réponses acceptées sont 4, 6, 8, 10, 12, 20 ou 100 "))
#Chosing the number of dice you want in a very ugly way (cancelled) 
#rolling de dice
    lance1 = random.randint(1, NbFace)
    lance11 = random.randint(1, NbFace)
    lance2 = random.randint(1, NbFace)
    lance21 = random.randint(1, NbFace) 
    Tirage1 = lance1 + lance11
    Tirage2 = lance2 + lance21
#God mode  
    if str(Player1) == "Dieu":
        lance1 = NbFace
        lance2 = NbFace
        Tirage1 = NbFace*Nbdee +1
    if str(Player2) == "Dieu":
        lance3 = NbFace
        lance4 = NbFace
        Tirage2 = NbFace*Nbdee +1
#as we want a winner at all cost    
    while Tirage1 == Tirage2 :
        print()
#Giving a more personal result for Player 1
    if Tirage1 <= NbFace * Nbdee / 2 :
        print(Player1 + " a obtenu un PETIT score de " + str(Tirage1) + " ! (" + str(lance1) + " + " + str(lance11)  + ")")
    if Tirage1 >= NbFace * Nbdee * 1.75 and Tirage1 <= NbFace * Nbdee :
        print(Player1 + " a obtenu un score IMPRESSIONNANT de " + str(Tirage1) + " ! (" + str(lance1) + " + " + str(lance11)  + ")")
    if Tirage1 >= NbFace * Nbdee +1 :
        print(Player1 + " a obtenu un score DIVIN de " + str(Tirage1) + "! (" + str(lance1) + " + " + str(lance11)  + ")")
    if Tirage1 < NbFace * Nbdee * 1.75 and Tirage1 > NbFace * Nbdee /2 :
        print(Player1 + " a obtenu un score de " + str(Tirage1) + " (" + str(lance1) + " + " + str(lance11)  + ")")
#Giving a more personal result for Player2
    if Tirage2 <= NbFace * Nbdee / 2 :
        print(Player2 + " a obtenu un PETIT score de " + str(Tirage2) + "! (" + str(lance2) + " + " + str(lance21)  + ")")
    if Tirage2 >=  NbFace * Nbdee * 1.75 and Tirage1 <= NbFace * Nbdee :
        print(Player2 + " a obtenu un score IMPRESSIONNANT de " + str(Tirage2) + " ! (" + str(lance2) + " + " + str(lance21)  + ")")
    if Tirage2 >= NbFace * Nbdee +1 :
        print(Player2 + " a obtenu un score DIVIN de " + str(Tirage2) + "! (" + str(lance2) + " + " + str(lance21)  + ")")
    if Tirage2 < NbFace * Nbdee * 1.75 and Tirage2 > NbFace * Nbdee /2 :
        print(Player2 + " a obtenu un score de " + str(Tirage2) + " (" + str(lance2) + " + " + str(lance21)  + ")")
    print()
#Getting a winner
    if Tirage1 > Tirage2:
        print(Player1 + " a gagné !")
    elif Tirage2 > Tirage1:
        print(Player2 + " a gagné !")
    print()
#Replay Part2    
    Rejouer = str(input("Voulez-vous rejouer ?  Oui ou Non "))
    valide = ["Oui", "Non"]
    while Rejouer not in valide:        
        Rejouer = str(input("Les réponses acceptées sont Oui ou Non "))
    if Rejouer == "Non":
        print()
    print()
print()
print()
print()
print()
print()
print()
print("Merci d'avoir participé aux Wild Rolling Dice School ! Au revoir et à bientôt !.")
#just to feed my ego a lil'
print("|    | _____  __    ___   ___  _____  ___  .    .")
print("|    |   |   |  \  |   | |   |   |   |   | |\   | ")
print("|====|   |   |   \ |   | |___|   |   |   | | \  | ")
print("|    |   |   |   / |   | |  \    |   |   | |  \ | ")
print("|    | __|__ |__/  |___| |   \ __|__ |___| |   \| ")

"""     Nbdee = int(input("Combien de dés voulez vous lancer (de 2 à 10) ? "))
    Nbdeepossible = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    while Nbdee not in Nbdeepossible:        
        Nbdee = int(input("Désolé mais tu dois choisir un chiffre qui est compris entre 2 et 10. "))"""

"""     Nbply = int(input("Combien de joueurs (de 2 à 10) ? "))
    Nbplypossible = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    while Nbply not in Nbplypossible:        
        Nbply = int(input("Désolé mais tu dois choisir un chiffre qui est compris entre 2 et 10. "))"""



