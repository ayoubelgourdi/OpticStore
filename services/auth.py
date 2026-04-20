from models.client import Client
from models.admin import Admin
import json

class Auth:
    def load_clients(self):
        with open("/home/ayoub/OpticStore/data/clients.json","r") as F:
            self.data_clients = json.load(F)

    def login_client(self):
        self.load_clients()
        
        while True:
            self.username = input("enter username : ")

            if self.username != "" and not " " in self.username:
                break

            return "> username not valide !"

        while True:
            self.password = input("enter password : ")

            if self.password != "" and not " " in self.password:
                break

            return "> password not valide !"
    
        for i in self.data_clients:
            if i["username"] == self.username and i["password"] == self.password:
                return Client(self.username, self.password)
                
        return False
    
    def register_client(self):

        while True:
            self.username = input("enter username : ")

            if self.username != "" and " " not in self.username:
                break

            print("> username not valide !")

        while True:
            self.password = input("enter password : ")

            if self.password != "" and " " not in self.password:
                break
            
            print("> password not valide !")

        new_client = {
            "username": self.username,
            "password": self.password
        }

        with open("/home/ayoub/OpticStore/data/clients.json","r") as F:
            data = json.load(F)

        data.append(new_client)

        with open("/home/ayoub/OpticStore/data/clients.json","w") as F:
            json.dump(data, F, indent=4)

    def login_admin(self):

        while True:
            self.username = input("enter username : ")

            if self.username != "" and not " " in self.username:
                break

            return "> username not valide !"

        while True:
            self.password = input("enter password : ")

            if self.password != "" and not " " in self.password:
                break

            return "> password not valide !"
        
        if self.username == "admin" and self.password == "admin":
            return Admin(self.username, self.password)