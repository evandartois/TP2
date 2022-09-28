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