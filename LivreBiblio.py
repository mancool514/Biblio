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
            for livre in resultat:
                if livre["disponible"]:
                    print("livre emprunter")
                    livre["quantite_totale"] -= 1
                    return livre["titre"]
                    
                else:
                    print("le livre est non disponible")
                    return -1

            if livre["quantite_totale"] == 0:
                livre["disponible"] = False

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