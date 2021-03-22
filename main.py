import random
import string
import re

#créer fonction qui va se charger de générer cette chaîne 
def generer_code_debloquage():
    #format AAA-2222-XX
    lettres = string.ascii_uppercase

    mot=''.join(random.choice(lettres) for i in range(4))
    numeros = random.randint(100,9999)
    chars =''.join(random.choice(lettres) for i in range(2))
    
    code = mot +"-" + str(numeros)+"-" + chars
    print("votre code débloquage est :", code)
    return code



# affichier parking status
def affcher_parking():
    #boucle parcourir chaque emplacemnt pur afficher la disponiblité
    for num_etage,etages in enumerate(parking,start=1):
        for num_place, place in enumerate(etages,start=1):
            resultat = ("non dispo","Disponible")[place =="D"]
            resultat = (resultat,"Réservé")[place=="H"]
            print("Etage n°-", num_etage, "place n°",num_place,resultat)

#log welcome
print("Bienvenue au niveau -1, que souhaitez-vous faire ?")



# creation de liste
emplacements = 27;
parking = ['D'] * emplacements # D pour place disponible 
etages = 3

parking = [['D'] * emplacements] * etages

#créer une liste  de dictonaire de code à débloqué
code_debloquage = [
    {},
    {},
    {}
]

for num_etage in enumerate(parking):
    #générer deux emplacemnts prioritaire au hasard
    emplacement1_hasard = random.randint(1,len(parking[num_etage])-1)
    emplacement2_hasard = random.randint(1,len(parking[num_etage])-1)

    parking[0][emplacement1_hasard] ='H'
    parking[0][emplacement2_hasard] ='H'

#recuperer l'emplacement n°3 du parking
emplacements_selection = parking[2]



#garer une voiture au 1er emplacement
parking[0][0] = 'V' # V pour place prise

#boucle parcourir chaque emplacemnt pur afficher la disponiblité
#affcher_parking()

while True:
    print("Choississez un numéro d'étage")

    
    choix_etage = int(input()) -1

    if choix_etage >=0 and choix_etage < len(parking):
        print("Vous avez choisi l'étage n°", choix_etage + 1)

        #proposer à notre client de faire une action
        print("1: Garer une voiture, 2: Récupérer une voiture")
        choix = int (input())

        #verifier le choix
        if choix == 1:
            print("Vous avez décider de Garer une voiture, choississer son emplacement")
            choix_emplacement = int(input())-1
            #verifier si la place est disponible
            if len(parking[choix_etage]) > choix_emplacement >0:

                #verifier si l'emplacement est H
                if parking[choix_etage][choix_emplacement] == 'H':
                    #demander son code
                    print("Quel est votre code prioritaire ?")
                    choix_code_h = input()

                    #verification du code
                    regex ) "^HP-[1-9]*-[a-z-A-Z]*"
                    verif = re.search(regex,string)

                    if verif is None:
                        print("vous n'avez pas le bon formatage")
                    else:
                        print("C'est OK!")
                        print("vous avez prit la place n°", choix_emplacement +1)
                        parking[choix_etage][choix_emplacement] ='V'
                        #générer le code secret 
                        code_secret = generer_code_debloquage()
                        code_debloquage[choix_etage][choix_emplacement] = code_secret
                        print(code_debloquage)


                elif parking[choix_etage][choix_emplacement] == "D":
                    print("vous avez prit la place n°", choix_emplacement +1)
                    parking[choix_etage][choix_emplacement] ='V'
                    #générer le code secret 
                    code_secret = generer_code_debloquage()
                    code_debloquage[choix_etage][choix_emplacement] = code_secret
                    print(code_debloquage)

                else:
                    print("Place non disponible ")
        elif choix == 2:
            print("Récupérer voiture, mettre le numéro de place:")

            choix_emplacement = int(input()) -1

            #verifier si la place exise
            if len(parking[choix_etage]) > choix_emplacement > 0:
                if parking[choix_etage][choix_emplacement] =='V':
                    #demander le code secret de la voiture
                    print("donnez le code secret")
                    choix_code_secret = input()

                    #verifier si le code est bon
                    code_secret_atrouver=code_debloquage[choix_etage][choix_emplacement]

                    if choix_code_secret == code_secret_atrouver:
                        print("Véhicule récupéré")
                        parking[choix_etage][choix_emplacement] = 'D'
                        print("L'emplacement n°", choix_emplacement +1,"est désormais disponible")
                    else: 
                        print("code incorrect")
                else:
                    print("Emplacemnt vide")
        else:
            print ("Error")
        #print parking
        #boucle parcourir chaque emplacemnt pur afficher la disponiblité
        affcher_parking()
    else: 
        print ("étages non existant")