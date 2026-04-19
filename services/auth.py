from models.client import Client
from models.admin import Admin
import json

class auth:
    def load_clients(self):
        with open("/home/ayoub/OpticStore/data/clients.json","r") as F:
            self.data_clients = json.load(F)

    def login_client(self):
        while True:
            username = input("enter username : ")
            if username != "" or not " " in username:
                break
            return "username not valide !"

        while True:
            password = input("enter password : ")
            if password != "" or not " " in password:
                break
            return "password not valide !"

        for i in self.data_clients:
            if i["username"] == username and i["password"] == password:
                Client(username, password)
                