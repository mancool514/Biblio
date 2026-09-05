import bcrypt

class Utilisateur:
    def __init__(self,username,password,livres_empruntes=None):
        self.username = username
        self.password = password
        self.livres_empruntes = livres_empruntes if livres_empruntes is not None else []

    def ajouter_livre(self,livre):
        if livre not in self.livres_empruntes:
            self.livres_empruntes.append(livre)
            return True
        else:
            return False

    def retirer_livre(self,livre):
        if livre in self.livres_empruntes:
            self.livres_empruntes.remove(livre)
            return True
        else:
            return False

    def verifier_mdp(self,mdp):
        mdp = mdp.encode("utf-8")
        hash_bytes = self.password.encode("utf-8") if isinstance(self.password, str) else self.password
        if bcrypt.checkpw(mdp,hash_bytes):
            return True
        else:
            return False

