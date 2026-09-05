import json


from Livre import Livre

class Bibliotheque:
    def __init__(self):
        self.bibliotheque = []
        self.chemin_fichier = "db/bibliotheque.json"
        self.chargement()

    def chargement(self):
        with open(self.chemin_fichier, "r") as file:
            self.fichier = json.load(file)
            for livre in self.fichier:
               self.bibliotheque.append(Livre(livre["id_livre"],livre["titre"],livre["auteur"],livre["quantite_totale"],livre["quantite_disponible"]))

    def rechercher(self,titre):
        titre = titre.lower().strip()
        resultat = [
            livre for livre in self.bibliotheque
            if titre in livre.titre.lower()
        ]
        return resultat[0] if len(resultat) > 0 else False

    def sauvegarde(self):
        donne_json = []
        with open(self.chemin_fichier, "w") as file:
            for i in self.bibliotheque:
                data = {
                    "id_livre": i.id_livre,
                    "titre": i.titre,
                    "auteur": i.auteur,
                    "quantite_totale": i.quantite_totale,
                    "quantite_disponible": i.quantite_disponible,
            }
                donne_json.append(data)
            json.dump(donne_json, file,indent=4)

