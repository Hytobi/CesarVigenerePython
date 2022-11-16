#Exercice 0:

from string import ascii_letters, digits
ACCENTS = 'àáâäèéêëìíîïòóôöùúûüç '
ALPHABET = ascii_letters + ACCENTS + ACCENTS.upper() + digits

#Exercice 1:

def input_mode() :
    '''Fonction qui demande de choisir entre cryptage et decryptage
       argument : None
       retour : retour le mode choisi'''
    terminer = False
    while not terminer :
        mode = input("Voulez-vous chiffrer ou déchiffrer un message (c/d) ?")
        if mode=="c" or mode=="C":
            print("chiffement")
            terminer = True
        elif mode=="d" or mode=="D" :
            print("déchiffement")
            terminer = True
        else :
            print("Option invalide")
    return mode



#Exercice 2:

def input_cle() :
    '''Fonction qui demande de choisir la clé de cryptage ou decryptage
       argument : None
       retour : clé de chiffrement'''
    terminer = False
    while not terminer :
        cle = int(input("Entrez la clé de chiffrement (1/104) :"))
        if 1<=cle or cle>=104 :
            terminer = True
        else :
            print("Option invalide")
    return cle




#Exercice 3 :

def pos(c) :
    '''Fonction qui donne la position d'une lettre dans la variable ALPHABET
       argument : c = str --- une lettre dont on veut savoir la position
       retour : retourne l’indice du caractère c dans l’alphabet. Sinon -1'''
    if len(c)==1:
        for i in range(len(ALPHABET)) :
            if ALPHABET[i]==c:
                message = i
                return message
    else :
        return -1   
    

#Exercice 4:

def car(n):
    '''Fonction qui donne la lettre dans la variable ALPHABET en fonction de la position voulu
       argument : n = int --- un entier dont on veut connaitre sa valeur dans ALPHABET
       retour : retourne le caractère à la position n dans l’alphabet'''
    return ALPHABET[n]

#Exercice 5 :

def chiffre_car(c,n) :
    '''Fonction qui donne la position d'une lettre dans la variable ALPHABET
       argument : c = str --- une lettre dont on veut savoir la position
                  n = int --- un entier dont on veut connaitre sa valeur dans ALPHABET
       retour : le chiffrement du caractère c par la clé n'''
    lettre = pos(c)
    lettre = lettre + n
    lettre_arrivee = car(lettre)
    return str(lettre_arrivee)

#Exercice 6 :

def cesar(message,mode,cle):
    '''Fonction qui chiffre ou déchiffre (selon la valeur de mode : 'c' ou 'd') la chaîne de caractères message à l’aide de cle
       argument : message = str --- le méssage a codé
                  mode = str --- chiffrage ou déchiffrage
                  cle = int --- la clé de chiffrement
       retour : Le message codé'''
    if mode=='c' or mode=='C':
        code = ''
        for j in range(len(message)) :
            if message[j]==' ':
                code = code + ' '
            else : 
                code = code + chiffre_car(message[j],cle)
        return code
    if mode=='d' or mode=='d' :
        decode = ''
        for j in range(len(message)) :
            if message[j]==' ':
                decode = decode + ' '
            else : 
                decode = decode + chiffre_car(message[j],-cle)
        return decode
        
#Exercice 7 :

def input_methode():
    '''Fonction qui  demande à l’utilisateur de choisir entre deux chiffrements : César ('c') ou Vigenère ('v')
       argument : None
       retour : La méthode de chiffrement choisie'''
    terminer = False
    while not terminer :
        x = input("Quelle méthode voulez-vous utiliser : Cesar (c) ou Vigenere (v) ?")
        if x=='c' or x=='v' :
            terminer = True
        else :
            print("Option invalide !")
    return x

#Exercice 8 :

def vigenere(message,mode,mot_cle):
    '''Fonction qui chiffre ou déchiffre, suivant la valeur de mode, message à l’aide de la clé mot_cle
       argument : message = str --- le méssage a codé
                  mode = str --- chiffrage ou déchiffrage
                  mot_cle = str --- la clé de chiffrement
       retour : Le message codé'''
    if mode=='c' or mode=='C':
        code = ''
        liste = []
        l = 0 
        for t in range(len(mot_cle)):
            k = pos(mot_cle[t])
            liste = liste + [k]
        for p in range(len(message)) :
            if message[p]==' ':
                code = code + ' '
                l = l-1
            else : 
                code = code + chiffre_car(message[p],liste[l])
                l = l + 1
                if l==len(mot_cle):
                    l=0
        return code
    if mode=='d' or mode=="D" :
        code = ''
        liste = []
        l = 0 
        for t in range(len(mot_cle)):
            k = pos(mot_cle[t])
            liste = liste + [k]
        for p in range(len(message)) :
            if message[p]==' ':
                code = code + ' '
                l = l-1
            else : 
                code = code + chiffre_car(message[p],-liste[l])
                l = l + 1
                if l==len(mot_cle):
                    l=0
        return code


#Exercice 9 :

def main():
    '''Fonction principale du programme'''
    message=input("Entrer votre message: ")
    mode=input("Voulez-vous chiffrer(c) ou déchiffrer(d) ce message ? ")
    if mode=="c" or mode=="C":
        cho1=input("Avec quelle méthode désirez-vous chiffrer le message ? Cesar(c) ou Vigenere(v) ")
        if cho1=="c" or cho1=="C":
            cle=int(input("Quelle est la clé ? "))
            solution=cesar(message,mode,cle)
            print(solution)
        elif cho1=="v" or cho1=="V":
            mot_cle=input("Quelle est le mot clé ? ")
            solution=vigenere(message,mode,mot_cle)
            print(solution)
        else:
            print("OPTION INALIDE !")
    elif mode=="d" or mode=="D":
        cho2=input("Avec quelle méthode désirez-vous chiffrer le message ? Cesar(c) ou Vigenere(v) ")
        if cho2=="c" or cho2=="C":
            cle=int(input("Quelle est la clé ? "))
            solution=cesar(message,mode,cle)
            print(solution)
        elif cho2=="v" or cho2=="V":
            mot_cle=input("Quelle est le mot clé ? ")
            solution=vigenere(message,mode,mot_cle)
            print(solution)
        else:
            print("OPTION INVALIDE !")
    
    










