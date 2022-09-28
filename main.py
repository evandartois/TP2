#TP1_evan_dartois&charlie_


#exo1
def palindrome():
    def palindrome(mot):
        lg = len(mot) #on calcule la longueur du mot
        if lg == 1: #si cette longueur est égale à 1, le mot est logiquement un palindrome
            return "Votre mot est un palindrome"
        elif lg > 1 and mot[0] == mot[-1]: #si la longueur du mot est supérieur à 1 et que la dernière lettre et la première du mot sont pareils
            return palindrome(mot[1:-1])  #par récursivité, on rappelle la fonction en enlevant la première et la dernière lettre
        else:
            return "Votre mot n'est pas un palindrome" #si la condition du elif n'est pas valide alors le mot n'est pas un palindrome
        
def lancement_palindrome():
    mot = input("entrez un mot :")  #on demande un mot à l'utilisateur
    print(palindrome(mot))  #affichage du return de la fonction palindrome
#lancement_palindrome()   #exo numéro 1



#exo2
def crypter(ch):
    ch_final = ''   #on crée une chaîne d'un ensemble vide 
    ch = ch.upper()   #on met la chaine en majuscules
    for lettre in ch:   #on prend lettre par lettre
        if ord(lettre) >= 65 and ord(lettre) < 90:    #avec l'aide de la table  ASCII, on vérifie que le caractère est bien une majuscule
            lettre = chr(ord(lettre)+1)  #si le contrôle est valide, on attribue à la lettre en question la lettre qui la suit 
            ch_final += lettre  #on ajoute cette lettre dans la chaîne crée initialement
        elif ord(lettre) == 90:  #si la lettre est un z
            lettre = 'A'         #on lui donne comme valeur la lettre A
            ch_final += lettre   #on ajoute par la suite à la chaîne final la letter A
        else:
            print('Le message contient des caractères spéciaux: cryptage impossible')  #si la chaine entrée par l'utilisateur n'a pas que des lettres, message d'erreur

    return ch_final  #on return la chaîne final cryptée

def lancement_crypter():
    chaine = input("ecrivez une chaîne de caractères :")  #on demande une chaîne à l'utilisateur
    print(crypter(chaine))  #affichage du return de la fonction crypter
#lancement_crypter()  #exo numéro2

#exo3
#1
def nb_min(password):
    nombre_minuscule = 0  #on initialise
    for carac in password:
        if ord(carac) >= 97 and ord(carac) <= 122:
            nombre_minuscule +=1

    return nombre_minuscule

#1
def nb_min(password):
    nombre_minuscule = 0
    for carac in password:
        if ord(carac) >= 97 and ord(carac) <= 122:
            nombre_minuscule +=1

    return nombre_minuscule

def nb_maj(password):
    nombre_majuscule = 0
    for carac in password:
        if ord(carac) >= 65 and ord(carac) <= 90:
            nombre_majuscule +=1

    return nombre_majuscule

def nb_alpha(password):
    nombre_non_alpha = 0
    for carac in password:
        if ord(carac) < 65 or (ord(carac) > 90 and ord(carac) < 97) or ord(carac) > 122:
            nombre_non_alpha +=1

    return nombre_non_alpha

def long_min(password):
    longueur_min = 0
    long_min_boucle = 0
    for carac in range(len(password)):
        if ord(password[carac]) >= 97 and ord(password[carac]) <= 122:
            long_min_boucle += 1
            if longueur_min < long_min_boucle:
                longueur_min = long_min_boucle
        else:
            long_min_boucle = 0
    return longueur_min

def long_maj(password):
    longueur_maj = 0
    long_maj_boucle = 0
    for carac in password:
        if ord(carac) >= 65 and ord(carac) <= 90:
            long_maj_boucle += 1
            if longueur_maj < long_maj_boucle:
                longueur_maj = long_maj_boucle
        else:
            long_maj_boucle = 0
    return longueur_maj

def score(password):
    bonus = (len(password)*4) + (nb_maj(password)*2) + (nb_min(password)*3) + (nb_alpha(password)*5)
    penalite = (long_min(password)*2) + (long_maj(password)*3)
    score = bonus - penalite
    return score

if __name__ == '__main__':
    """
    mot = input("entrez un mot :")
    print(palindrome(mot))

    chaine = input('Ecrivez un message ')
    print(crypter((chaine)))
    """
    pw = input('Donner votre mot de passe ')
    # print(len(pw))
    # print(nb_min(pw))
    # print(nb_maj(pw))
    # print(nb_alpha(pw))
    # print(long_min(pw))
    # print(long_maj(pw))
    print(score(pw))
