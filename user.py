import json
import bcrypt


class User:
    def __init__(self):
        with open("db/utilisateur.json", "r") as file:
            self.users = json.load(file)

    def login(self):
        self.user_name = input("entrez votre nom d'utilisatuer >>> ")
        if self.user_name == "-a":
            self.add_user()


        mdp = input("entrez votre mot de passe >>> ")

        mdp = mdp.encode("utf-8")
        encoded_mdp = self.users[self.user_name]["mot_de_passe"].encode("utf-8")

        if bcrypt.checkpw(mdp, encoded_mdp):
            print("login reussi")
            self.emprunt = self.users[self.user_name]["emprunt"]
            return True
        else:
            return False

    def logout(self):
        self.users[self.user_name]["emprunt"] = self.emprunt
        with open("db/utilisateur.json", "w") as file:
            json.dump(self.users, file, indent=4)

    def change_mdp(self):
        input1 = input("entrez votre nouveau mot de passe >>> ")
        input2 = input("entrez le a nouveau >>> ")
        if input1 == input2:
            input2 = input2.encode("utf-8")
            salt = bcrypt.gensalt()
            hashed_bytes = bcrypt.hashpw(input2, salt)

            self.users[self.user_name]["mot_de_passe"] = hashed_bytes.decode("utf-8")

    def add_user(self):
        user = input("entrez votre nom dutilisatuer >>> ")
        pwd = input("entrez votre mot de passe >>> ")
        pwd = pwd.encode("utf-8")
        salt = bcrypt.gensalt()
        mdp = bcrypt.hashpw(pwd, salt)
        
        db = {
            f"{user}": {
                "mot_de_passe": mdp.decode("utf-8"),
                "emprunt": []
            }
        }

        
        self.users.update(db)
        with open("db/utilisateur.json", "w") as file:
            json.dump(self.users, file, indent=4)
        quit()