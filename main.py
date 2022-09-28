#exo1
def palindrome():
    def palindrome(mot):
        lg = len(mot)
        if lg == 1:
            return "Votre mot est un palindrome"
        elif lg > 1 and mot[0] == mot[-1]:
            return palindrome(mot[1:-1])
        else:
            return "Votre mot n'est pas un palindrome"

#exo2
def crypter(ch):
    ch_final = ''
    ch = ch.upper()
    for lettre in ch:
        if ord(lettre) >= 65 and ord(lettre) < 90:
            lettre = chr(ord(lettre)+1)
            ch_final += lettre
        elif ord(lettre) == 90:
            lettre = 'A'
            ch_final += lettre
        else:
            print('Le message contient des caractères spéciaux: cryptage impossible')

    return ch_final

#exo3
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
        if ord(carac) <= 65 or (ord(carac) >= 90 and ord(carac) <= 97) or ord(carac) >= 122:
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

if __name__ == '__main__':
    """
    mot = input("entrez un mot :")
    print(palindrome(mot))

    chaine = input('Ecrivez un message ')
    print(crypter((chaine)))
    """
    ps = 'MAL-LDKHHIHIOD-JH'
    print(nb_min(ps))
    print(nb_maj(ps))
    print(nb_alpha(ps))
    print(long_min(ps))
    print(long_maj(ps))
