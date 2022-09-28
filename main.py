def palindrome(mot):
    lg=len(mot)
    if lg==1 :
        return "Votre mot est un palindrome"
    elif lg>1 and mot[0] == mot[-1]:
        return palindrome(mot[1:-1])
    else :
        return "Votre mot n'est pas un palindrome"


def lancement_palindrome():
    mot = input("entrez un mot :")
    print(palindrome(mot))
#lancement_palindrome()
#exo numéro 1

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
def nb_min(passeword):
    nombre_minuscule = 0
    for carac in passeword:
        if ord(carac) >= 97 and ord(carac) <= 122:
            nombre_minuscule +=1

    return nombre_minuscule

def nb_maj(passeword):
    nombre_majuscule = 0
    for carac in passeword:
        if ord(carac) >= 65 and ord(carac) <= 90:
            nombre_majuscule +=1

    return nombre_majuscule

def nb_alpha(passeword):
    nombre_non_alpha = 0
    for carac in passeword:
        if ord(carac) <= 65 or (ord(carac) >= 90 and ord(carac) <= 97) or ord(carac) >= 122:
            nombre_non_alpha +=1

    return nombre_non_alpha

if __name__ == '__main__':
    """
    chaine = input('Ecrivez un message ')
    print(crypter((chaine)))
    """
    ps = 'chrfdfORID16516é"*'
    print(nb_min(ps))
    print(nb_maj(ps))
    print(nb_alpha(ps))
