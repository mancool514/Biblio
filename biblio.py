import json

import json

class LivreBiblio:
    def __init__(self,titre,annee,):
        self.titre = titre
        self.annee = annee
        self.emprunte = False

    def emprunter(self):
        if not self.emprunte:
            self.emprunte = True
            return True
        else:
            return False


    def rendre(self):
        if self.emprunte:
            self.emprunte = False
            return False
        else:
            return True

polo = LivreBiblio("polo",2009)
print(polo.emprunter())
print(polo.emprunter())
print(polo.rendre())




def test_utilisateurs(individu, dictionnaire_users):
    if not dictionnaire_users or individu not in dictionnaire_users:
        return False
    return True

def sauvegarder(file_sauvegarder,quoi):
    with open(file_sauvegarder, "w") as files:
        json.dump(quoi, files, indent=4)

def charger(file_charger):
    try:
        with open(file_charger, "r") as files:
            return json.load(files)
    except FileNotFoundError:
        return {}

def ajouter_livre(livre,annee_ecriture,dictionnaire_livre):
    if livre in dictionnaire_livre:
        return "Nous avons déjà ce livre."
    else:
        dictionnaire_livre[livre] = {
            "année": annee_ecriture,
            "emprunte": False
             }
        return "Merci pour cet ajout! Livre ajouté: " + livre + ", Année de publication: " + str(annee_ecriture)

def emprunter_livre(livre,qui, dictionnaire_livre, dictionaire_utilisateur):
    if livre in dictionnaire_livre:
        if not dictionnaire_livre[livre]["emprunte"]:
            if len(dictionaire_utilisateur[qui]) >= 4:
                return "Vous avez trop de livres."
            else:
                dictionaire_utilisateur[qui].append(livre)
                dictionnaire_livre[livre]["emprunte"] = True
                return "Livre emprunté !"
        else:
            return "Livre déjà emprunté."
    else:
        return "Livre introuvable"

def rendre_live(livre,qui, dictionnaire_livre, dictionnaire_utilisateur):
    if livre in dictionnaire_livre:
        if livre in dictionnaire_utilisateur[qui]:
            if dictionnaire_livre[livre]["emprunte"]:
                dictionnaire_livre[livre]["emprunte"] = False
                dictionnaire_utilisateur[qui].remove(livre)
                return "Livre remis!"
            else:
                return "Livre déjà remis."
        else:
            return "Vous n'avez pas ce livre"
    else:
        return "Livre introuvable"

utilisateur = charger("utilisateur.json")
biblio = charger("livre.json")

while True:
    try:
        choix1 = int(input("\n1. Ajouter un livre\n2. Ajouter un utilisateur\n3. Emprunter un livre\n4. Rendre un livre\n5. Voir les livres disponibles\n6 .Voir les livres empruntés par un utilisateur\n7 .Quitter"))
    except ValueError:
        print("Vous devez rentrer un chiffre entre 1 et 7.")
        continue

    if choix1 == 1:
        donnateur = input("Qui êtes-vous?")
        test_ajouter_livre = test_utilisateurs(donnateur,utilisateur)
        if not test_ajouter_livre:
            print("Utilisateur introuvable")
            continue
        else:
            print(f"Bienvenu {donnateur}")
            livre_ajouter = input("Quel livre voulez-vous ajouter?")
            try:
                annee = int(input("Quel est l'année de publication du livre?"))
            except ValueError:
                print("Vous devez rentrer une année.")
                continue
            print(ajouter_livre(livre_ajouter, annee, biblio))
            sauvegarder("livre.json", biblio)
            
    elif choix1 == 2:
        nom = input("Quel est votre nom?")
        if nom not in utilisateur:
            utilisateur[nom] = []
            sauvegarder("utilisateur.json",utilisateur)
            print("Utilisateur ajouté:", nom)
        else:
            print("Ce nom est déjà utilisé.")
            
    elif choix1 == 3:
        if len(biblio) == 0:
            print("Aucun livre")
            continue
        emprunteur = input("Qui êtes-vous?")
        test_emprunter_livre = test_utilisateurs(emprunteur,utilisateur)
        if not test_emprunter_livre:
            print("Utilisateur introuvable")
            continue
        else:
            print(f"Bienvenu {emprunteur}")
            livre_emprunte = input("Quelle livre voulez-vous emprunter?")
            print(emprunter_livre(livre_emprunte,emprunteur,biblio,utilisateur))
            if biblio[livre_emprunte]["emprunte"]:
                sauvegarder("livre.json", biblio)
                sauvegarder("utilisateur.json", utilisateur)
            else:
                continue
                
    elif choix1 == 4:
        if len(biblio) == 0:
            print("Aucun livre")
            continue
        redonneur = input("Qui êtes-vous?")
        test_rendre_livre = test_utilisateurs(redonneur,utilisateur)
        if not test_rendre_livre:
            print("Utilisateur introuvable")
            continue
        else:
            print(f"Bienvenu {redonneur}")
            livre_remis = input("Quelle livre voulez-vous remettre?")
            print(rendre_live(livre_remis,redonneur,biblio,utilisateur))
            if not biblio[livre_remis]["emprunte"]:
                sauvegarder("livre.json", biblio)
                sauvegarder("utilisateur.json", utilisateur)
            else:
                continue
                
    elif choix1 == 5:
        if len(biblio) == 0:
            print("Aucun livre")
        else:
            for key in biblio.items():
                print(key)
                
    elif choix1 == 6:
        if len(utilisateur) == 0:
            print("Aucun utilisateur")
        else:
            print(utilisateur)
            
    elif choix1 == 7:
        break


