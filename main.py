from livrebiblio import LivreBiblio
from user import User

user = User()
biblio = LivreBiblio()

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

def user_input(mode):
    if mode == 1:
        return input("que voulez vous faire\n1: emprunter\n2: chercher\n3: retourner un livre\n4: changer le mot de passe\n5: voir cest emprunt actif \n6: quitter \n>>> ")
    if mode == 2:
        return input("que voulez vous faire\n1: ajouter un livre\n2: retirer un livre\n3: surpimer un utilisateur\n4: quitter \n>>> ")

def print_emprunt():
    for i in user.emprunt:
        print(i)

def main():
    if not user.login():
        raise PermissionError("mot de passe ou nom dutilisateur invalide")

    if user.user_name == "sudo":
        while True:
            choix = user_input(2)
            match choix:
                case "1":
                    biblio.add_livre()
                case "2":
                    biblio.retirer_livre()
                case "3":
                    user.delete_user()
                case "4":
                    break
                case _:
                    print("commande non reconnu")
            print("\n")
    else:
        while True:
            choix = user_input(1)
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
                    break
                case _:
                    print("commande non reconnu")
            print("\n")
    
    user.logout()


if __name__ == "__main__":
    main()