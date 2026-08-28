from biblio import LivreBiblio
from user import User

user = User()
biblio = LivreBiblio()

if not user.login():
    raise PermissionError("mot de passe ou nom dutilisateur invalide")



def emprunt():
    livre = biblio.emprunter()
    if livre == -1:
        raise ValueError("le livre existe pas")
    
    user.emprunt.append(livre.lower().strip())
    print(user.emprunt)

def rendre():
    titre = biblio.rendre()
    print(titre)
    if titre == -1:
        raise ValueError("le livre existe pas")

    if titre not in user.emprunt:
        biblio.reverse_emprunt(titre)
        raise ValueError("vous navez pas ce livre")

    user.emprunt.remove(titre)

def user_input():
    return input("que voulez vous faire\n1: emprunter\n2: chercher\n3: retourner un livre\n4: changer le mot de passe\n5: voir cest emprunt actif \n6: quitter \n>>> ")

def print_emprunt():
    for i in user.emprunt:
        print(i)

def main():
    choix = user_input()
    match choix:
        case "1":
            emprunt()
        case "2":
            biblio.search()
        case "3":
            rendre()
        case "4":
            user.change_mdp()
        case "5":
            print_emprunt()
        case "6":
            user.logout()
            break
        case _:
            print("commande non reconnu")
