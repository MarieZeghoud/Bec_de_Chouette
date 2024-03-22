#On importe les librairies Python nécéssaires
import random, time 


#On créée une fonction règle pour introduire les règles aux joueurs 
def regles():
  choix = input("Voulez-vous lire les règles avant de commencer ? (oui/non)")
  #les joueurs acceptent
  if choix == "oui":
    print()
    print("Le Bec de la Chouette se joue avec trois dés à 6 faces.")
    #On utilise time.sleep pour définir le délai d'apparition de chaque ligne print
    time.sleep(2)
    print("Avant de commencer, chaque joueur lance un dé: celui avec le plus petit score commence.")
    time.sleep(2)
    print("Durant le tour d'un joueur, celui-ci lance ses trois dés.")
    time.sleep(2)
    print("En fonction du résultat, plusieurs combinaisons sont possbles")
    print()
    time.sleep(2)
    print("- La Chouette: deux dés identiques ==> carré du nombre en commun.")
    time.sleep(2.5)
    print("Vous pouvez alors tenter une Grelottine pour doubler le score obtenu ce tour.")
    print()
    time.sleep(2.5)
    print("- La Velute: la somme des deux premiers dés vaut le 3e ==> double du carré du 3e dé.")
    time.sleep(2.5)
    print("Vous pouvez alors tenter un Sirop pour tripler le score obtenu ce tour.")
    print()
    time.sleep(2.5)
    print("- La Suite : trois dés forment une suite ==> score nul, le tour passe au joueur suivant.")
    print()
    time.sleep(2.5)
    print("- Le Néant: aucune combinaison ==> somme des dés.")
    print()
    time.sleep(2.5)
    print("Le premier joueur à dépasser les 343 points gagne la partie.")
    time.sleep(2)
    print()
    print("Lorsque vous aurez fini de lire, appuyez sur Entrée pour commencer.")
    #On laisse le joueur valider avec un input vide
    input()
    print()
    print()
    print()
  #les joueurs refusent
  elif choix == "non":
    print("La partie peut donc commencer.")
    print()
    time.sleep(1)
  #La réponse n'est pas correcte
  else:
    print("Erreur ! Répondez seulement par oui, ou non !")
    print()
    time.sleep(1)
    #On redirige le joueur au début de la fonction
    regles()
###   


  
#Introduction du jeu
print("Bienvenue sur la version Python du Bec de la Chouette.")
time.sleep(1)
print("Cette version du jeu se joue à 2 joueurs.")
time.sleep(1)
#On demande aux joueurs s'ils veulent voir les règles
regles()
#La partie commence
print("Nous allons maintenant procéder au lancer de dés...")
time.sleep(1)
print("Le joueur avec le plus petit score commence.")
print()
time.sleep(1)


###On définit les variables principales
#Les scores des deux joueurs
ScoreJ1 = 0
ScoreJ2 = 0
#Les dfférents dés et leurs résultats
diceA = 0
diceB = 0
diceC = 0
diceD = 0
#La somme des dés
TotalDes = 0


#Programmation des variables 


#On programme le lancement des dés
def roll():
 #On rend les variables globales afin qu'elles soient interprétées par les fonctions 
 global diceA, diceB, diceC, diceD
 global diceTab
 #On génère aléatoirement les résultats avec random
 diceA = random.randint(1,6) 
 diceB = random.randint(1,6) 
 diceC = random.randint(1,6)
 print(diceA, diceB, diceC)
 time.sleep(1)
 #On met les résultats dans une liste
 diceTab = [diceA, diceB, diceC]
 #On trie la liste ( pour détecter une Suite )
 diceTab.sort()
###


#La Grelotte, en cas de Chouette
def grelotte():
  global TotalDes
  global diceA, diceB, diceC, diceD
  global diceTab
  choix = str(input("Voulez vous relancer un dé pour tenter une Grelottine ? (oui/non)"))
  #Le joueur accepte
  if choix == "oui":
    print("Vous relancez un de vos dés...")
    time.sleep(1)
    print()
    #On lance un 4e dé, le dé de relance
    diceD = random.randint(1,6) 
    print(diceD)
    time.sleep(1)
    #le joueur a gagné
    if diceD == diceTab[1]:
      print("Vous avez réussi ! Votre score pour ce tour est doublé")
      time.sleep(1)
      #Double du carré du nombre
      TotalDes = TotalDes + diceTab[1]**2
    #Le joueur a raté
    elif diceD != diceTab[1]:
      print("Raté ! Vous gardez les points de votre Chouette.")
      time.sleep(1)
  #Refusé
  elif choix == "non":
    print("Vous conservez votre score actuel.")
    time.sleep(1)
  #Mauvaise commande
  else:
    print("Erreur ! Répondez seulement par oui, ou non !")
    time.sleep(1)
    #On redirige le joueur au début de la fonction
    grelotte()
###


#La Chouette
def chouette():
  global TotalDes
  global diceA, diceB, diceC, diceD
  global diceTab
  print("Vous avez une Chouette !")
  time.sleep(1)
  print("Vous obtenez le carré du nombre récurrent.")
  #Le carré du nombre
  TotalDes = diceTab[1]**2
  time.sleep(1)
  #On permet au joueur de tenter ou non une grelotte 
  grelotte()
###

  
#Le Sirop, en cas de Velute 
def sirop():
  global TotalDes
  global diceA, diceB, diceC, diceD
  global diceTab
  choix = str(input("Voulez vous relancer un dé pour tenter un Sirop ? (oui/non)"))
  if choix == "oui":
    print("Vous relancez un de vos dés...")
    time.sleep(1)
    print()
    #On lance un 4e dé, le dé de relance
    diceD = random.randint(1,6) 
    print(diceD)
    time.sleep(1)
    #le joueur a gagné
    if diceD == diceC:
      print("Vous avez réussi ! Votre score pour ce tour est triplé")
      time.sleep(1)
      #triple du double du carré du nombre
      TotalDes = TotalDes * 3 
    #Le joueur a raté
    elif diceD != diceC:
      print("Raté ! Vous conservez votre score actuel.")
      time.sleep(1)
  #Refusé
  elif choix == "non":
    print("Vous conservez les points de votre Velute.")
    time.sleep(1)
  #Mauvaise commande
  else:
    print("Erreur ! Répondez seulement par oui, ou non !")
    time.sleep(1)
    #On redirige le joueur au début de la fonction
    sirop()
###


#La Velute
def velute():
  global TotalDes
  global diceA, diceB, diceC, diceD
  global diceTab
  print("Vous avez une Velute !")
  time.sleep(1)
  print("Vous obtenez le double du carré du 3e dé.")
  #le double du carré du 3e dé
  TotalDes = 2 * (diceC**2)
  time.sleep(1)
  #On permet au joueur de tenter ou non un Sirop
  sirop()
###


#Le bec de Chouette
def becdechouette():
  global TotalDes
  global diceA, diceB, diceC, diceD
  global diceTab
  print("Vous avez un Bec de Chouette !")
  time.sleep(1)
  print("Vous obtenez la somme de 40 et du chiffre récurrent x 10.")
  time.sleep(1)
  #40 + 10 × (le Bec de Chouette)
  TotalDes = 40 + 10 * diceA
###


#La Suite
def suite():
  global TotalDes
  global diceA, diceB, diceC, diceD
  global diceTab
  print("Vous avez une Suite !")
  time.sleep(1)
  print("Vous n'obtenez aucun point supplémentaire.")
  time.sleep(1)
###

    
#Aucune combinaison
def neant():
  global TotalDes
  global diceA, diceB, diceC, diceD
  global diceTab
  print("Aucune combinaison spéciale: Néant !")
  time.sleep(1)
  print("Vous obtenez la somme de vos dés.")
  time.sleep(1)
  #Somme des dés
  TotalDes = diceA + diceB + diceC
###

#Score du Joueur 1
def resultJ1():
  global ScoreJ1, ScoreJ2
  global diceA, diceB, diceC, diceD
  global diceTab
  global TotalDes
  #On additionne les points obtenus durant ce tour au score total
  ScoreJ1 = ScoreJ1 + TotalDes
  print("Votre score est de", ScoreJ1)
  time.sleep(1)
  print()
  TotalDes = 0
###


#Score du Joueur 2
def resultJ2():
  global ScoreJ1, ScoreJ2
  global diceA, diceB, diceC, diceD
  global diceTab
  global TotalDes
  #On additionne les points obtenus durant ce tour au score total
  ScoreJ2 = ScoreJ2 + TotalDes
  print("Votre score est de", ScoreJ2)
  time.sleep(1)
  print()
  TotalDes = 0
###


###On crée la boucle de jeu 


#On définit le tour du joueur 1
def TurnJ1(): 
  global ScoreJ1, ScoreJ2
  global diceA, diceB, diceC, diceD
  global diceTab
  global TotalDes
  print("Joueur 1, vous lancez 3 dés (Touche Entrée).")
  #On laisse le joueur valider avec un input vide
  input()
  #Lancement des dés
  roll()
  #Combinaisons
  if diceTab[0] == diceTab[1] and diceTab[1] != diceTab[2] or diceTab[1] == diceTab[2] and diceTab[0] != diceTab[1]:
    chouette() 
  elif diceA + diceB == diceC:
    velute()  
  elif (diceTab[0] + 2) == (diceTab[1] + 1) == diceTab[2] or (diceTab[2] + 2) == (diceTab[1] + 1) == diceTab[0]:
    suite()    
  elif diceA == diceB == diceC:
    becdechouette()     
  else:
    neant()
  #Total des points
  resultJ1()
###


#On définit le tour du joueur 2
def TurnJ2():
  global ScoreJ2, ScoreJ1
  global diceA, diceB, diceC, diceD
  global diceTab
  global TotalDes
  print("Joueur 2, vous lancez 3 dés (Touche Entrée).")
  #On laisse le joueur valider avec un input vide
  input()
  #Lancement des dés
  roll()
  #Combinaisons
  if diceTab[0] == diceTab[1] and diceTab[1] != diceTab[2] or diceTab[1] == diceTab[2] and diceTab[0] != diceTab[1]:
    chouette()
  elif diceA + diceB == diceC:
    velute()
  elif (diceTab[0] + 2) == (diceTab[1] + 1) == diceTab[2] or (diceTab[2] + 2) == (diceTab[1] + 1) == diceTab[0]:
    suite()
  elif diceA == diceB == diceC:
    becdechouette()
  else:
    neant() 
  #Total des points
  resultJ2()
### 


#On génère les lancers de dés des 2 joueurs
ScoreJ1 = random.randint(1,6) 
print("Le joueur 1 a obtenu un score de", ScoreJ1)
time.sleep(1)
ScoreJ2 = random.randint(1,6) 
print("Le joueur 2 a obtenu un score de", ScoreJ2)
time.sleep(1)
#Il y a égalité 
if ScoreJ1 == ScoreJ2: 
   print()
   time.sleep(1)
   print("Égalité: les dés vont êtres relancés.")
   print()
  #On relance jusqu'à départager les deux joueurs
   while ScoreJ1 == ScoreJ2: 
      ScoreJ1 = random.randint(1,6) 
      ScoreJ2 = random.randint(1,6)
   time.sleep(1)
   print("Le joueur 1 a obtenu un score de", ScoreJ1)
   time.sleep(1)
   print("Le joueur 2 a obtenu un score de", ScoreJ2)
   time.sleep(1)
  
###Il n'y a pas d'égalité

#Le joueur 1 commence 
if ScoreJ1 < ScoreJ2: 
 print()
 print("Joueur 1, vous commencez.")
 print()
 time.sleep(1)
 #On reset les scores
 ScoreJ1 = 0
 ScoreJ2 = 0
 #On définit la boucle de jeu
 while ScoreJ1 < 343 and ScoreJ2 < 343:
  TurnJ1()
  TurnJ2()
   #Conditions de victoire
  if ScoreJ1 >= 343: 
    print("Le joueur 1 a gagné !")
    break 
  elif ScoreJ2 >= 343:
    print("Le joueur 2 a gagné !")
    break
    
#Le joueur 2 commence 
elif ScoreJ2 < ScoreJ1: 
 print()
 print("Joueur 2, vous commencez.")
 print()
 time.sleep(1)
 #On reset les scores
 ScoreJ1 = 0
 ScoreJ2 = 0
 #On définit la boucle de jeu
 while ScoreJ1 < 343 and ScoreJ2 < 343:
   TurnJ2()
   TurnJ1()
   #Conditions de victoire
   if ScoreJ1 >= 343: 
     print("Le joueur 1 a gagné !")
     break 
   elif ScoreJ2 >= 343:
     print("Le joueur 2 a gagné !")
     break
###   