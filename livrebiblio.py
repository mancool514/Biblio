import json


class LivreBiblio:
    def __init__(self):
        with open("db/livre.json", "r") as file:
            self.data = json.load(file) # ouvre la base de donne et la met sous forme dun dictionaire a linitialisation de la classe

    def get_input(self):
        self.user_input = input("entrez le nom du livre ou l'auteur >>> ")
        return self.user_input
    
    def search(self):        # la fonction a pour but de fair eune recherche dans la base de donne et retourner a lutilisateur les resultats
        self.user_input = self.get_input().lower().strip()
        resultat = [
            livre for livre in self.data
            if self.user_input in livre["titre"].lower() or self.user_input in livre["auteur"].lower()
        ]

        if resultat:
            print(f"\n{len(resultat)} livre(s) trouver(s) : ")

            for livre in resultat:
                statut = "Disponible" if livre["disponible"] else "Non disponible"
                print(f"- {livre['titre']} (Auteur: {livre['auteur']}, Stock: {livre['quantite_totale']}, Statut: {statut})")
        else:
            print("Aucun livre ne correspond a votre recherche.")

    def emprunter(self):
        titre = self.get_input()
        titre = titre.lower().strip()
        resultat = [
            livre for livre in self.data
            if titre in livre["titre"].lower()
        ]

        if resultat:
            for titre in resultat:
                if titre["disponible"]:
                    print("livre emprunter")
                    titre["quantite_totale"] -= 1
                    return titre["titre"]
                    
                else:
                    print("le livre est non disponible")
                    return -1

            if titre["quantite_totale"] == 0:
                titre["disponible"] = False
            return -1

        else:
            print("le livre n'existe pas")
            return -1



    def rendre(self):
        titre = self.get_input()
        titre = titre.lower().strip()

        resultat = [
            livre for livre in self.data
            if titre in livre["titre"].lower()
        ]

        if resultat:

            for livre in resultat:
                if not livre["disponible"]:
                    livre["disponible"] = True

                livre["quantite_totale"] += 1
            return titre

        else:
            print("le livre existe pas")
            return -1


    def reverse_emprunt(self, titre):
        titre = titre.lower().strip()
        
        resultat = [
            livre for livre in self.data
            if titre in livre["titre"].lower()
        ]

        if resultat:
            for livre in resultat:
                if livre["disponible"]:
                    livre["disponible"] = False

                livre["quantite_totale"] -= 1

        else:
            print("le livre existe pas")

    def print_data(self):
        print(self.data)

    def save_file(self):
        with open("db/livre.json", "w") as file:
            json.dump(self.data, file, indent=4)

    def add_livre(self):
        titre = input("entrez le titre du livre >>> ")
        auteur = input("entrez l'auteur >>> ")
        qte = input("entrez la quantite disponible >>>")
        dispo = input("est il disponible en ce moment [Y/N] >>> ")
        id = input("entrez l'id du livre >>> ")

        if dispo == "Y" or dispo == "y" or dispo == "yes":
            dispo = True

        else:
            dispo = False

        new_book = {
            "id": id,
            "titre": titre,
            "auteur": auteur,
            "quantite_totale": qte,
            "disponible": dispo
        }

        self.data.append(new_book)
        self.save_file()

    def retirer_livre(self):
        book = self.get_input().lower().strip()
        resultat = [
            livre for livre in self.data
            if book in livre["titre"].lower()
        ]

        if resultat:
            for livre in resultat:
                info = {
                    "id": livre["id"],
                    "titre": livre["titre"],
                    "auteur": livre["auteur"],
                    "quantite_totale": livre["quantite_totale"],
                    "disponible": livre["disponible"]
                }
            if info in self.data:
                print(info)
                self.data.remove(info)
            
        self.save_file()