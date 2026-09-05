class Livre:
    def __init__(self, id_livre, titre, auteur, quantite_totale,quantite_disponible=None):
        self.id_livre = id_livre
        self.titre = titre
        self.auteur = auteur
        self.quantite_totale = quantite_totale
        self.quantite_disponible = quantite_disponible if quantite_disponible is not None else quantite_totale

    def rendre_exemplaire(self):
        if self.quantite_disponible < self.quantite_totale:
            self.quantite_disponible += 1
            return True
        return False

    def retirer_exemplaire(self):
        if self.quantite_disponible > 0:
            self.quantite_disponible -= 1
            return True
        return False

    def est_disponible(self):
        return self.quantite_disponible > 0
    def afficher_stock(self):
        return self.quantite_disponible

