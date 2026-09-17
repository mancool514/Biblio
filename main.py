from Bibliothèque import Bibliotheque
from gestionnaire_utilisateurs import GestionnaireUtilisateurs


gestionnaireutilisateurs = GestionnaireUtilisateurs()
bibliotheque = Bibliotheque()

def inscription(username, password):
    if gestionnaireutilisateurs.ajouter_utilisateur(username,password):
        gestionnaireutilisateurs.sauvegarde()
        return f"Merci de vous être inscrit, {username}"
    else:
        return "Nom d'utilisateur pris"

def rechercher_livre(livre):
    livre_objet = bibliotheque.rechercher(livre)
    if livre_objet:
        liste_livre_objet = []
        for livre in livre_objet:
            liste_livre_objet.append(livre.titre)
        return  liste_livre_objet
    else:
        return "Livre non retrouvé"

def voir_livres_emprunter(utilisateur):
    return utilisateur.livres_empruntes

def emprunter_livre(livre,utilisateur):
    livre_objet = bibliotheque.rechercher(livre)[0]
    if livre_objet:
        if livre_objet.est_disponible():
            if not len(utilisateur.livres_empruntes) >= 4:
                if utilisateur.ajouter_livre(livre_objet.titre):
                    if not livre_objet.retirer_exemplaire():
                        utilisateur.retirer_livre(livre_objet.titre)
                        return "Il y a eu un problème"
                    else:
                        bibliotheque.sauvegarde()
                        gestionnaireutilisateurs.sauvegarde()
                        return f"{livre} a été emprunté"
                else:
                    return "Vous avez déjà ce livre"
            else:
                return "Vous avez trop de livres"
        else:
            return "Livre non disponible"
    else:
        return "Livre non retrouvé"

def retourner_livre(livre,utilisateur):
    livre_objet = bibliotheque.rechercher(livre)
    if livre_objet:
        if utilisateur.retirer_livre(livre_objet.titre):
            if livre_objet.rendre_exemplaire():
                bibliotheque.sauvegarde()
                gestionnaireutilisateurs.sauvegarde()
                return f"{livre} a été rendu"
            else:
                utilisateur.ajouter_livre(livre_objet.titre)
                return "Il y a eu un problème"
        else:
            return "Vous n'avez pas ce livre"
    else:
        return "Livre non retrouvé"

def main():
    while True:
        choix_non_connecte = input("\n1.S'inscrire\n2.Se connecter\n3.Quitter")
        if choix_non_connecte == "1":
            new_u_username = input("\nNom de l'utilisateur : ")
            new_u_password = input("\nMot de passe : ")
            print(inscription(new_u_username, new_u_password))
        elif choix_non_connecte == "2":
            username_connexion = input("\nNom de l'utilisateur : ")
            password_connexion = input("\nMot de passe : ")
            utilisateur_connecte = gestionnaireutilisateurs.connexion(username_connexion, password_connexion)
            if utilisateur_connecte:
                while True:
                    choix_connecte = input("\n1.Rechercher un livre\n2.Emprunter un livre\n3.Retourner un livre\n4.Voir mes livres empruntés\n5.Quitter")
                    match choix_connecte:
                        case "1":
                            livre_rechercher = input("Entrer le nom du livre: ")
                            print(rechercher_livre(livre_rechercher))
                        case "2":
                            livre_empruner = input("Entrer le nom du livre: ")
                            print(emprunter_livre(livre_empruner,utilisateur_connecte))
                        case "3":
                            livre_rendu = input("Entrer le nom du livre: ")
                            print(retourner_livre(livre_rendu,utilisateur_connecte))
                        case "4":
                           print(voir_livres_emprunter(utilisateur_connecte))
                        case "5":
                            break
                        case _:
                            print("commande non reconnu")
            else:
                print("Mauvais nom d'utilisateur ou mot de passe")
        elif choix_non_connecte == "3":
            break

        else:
            print("\nEntrée invalide")
            break
if "__main__" == __name__:
    main()