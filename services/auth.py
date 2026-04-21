from models.client import Client
from models.admin import Admin
from utils.validation import v_username
from utils.validation import v_password
from utils.validation import v_price
from utils.validation import v_quantity
import json

class Auth:
    def load_clients(self):
        with open("/home/ayoub/OpticStore/data/clients.json","r") as F:
            self.data_clients = json.load(F)

    def login_client(self):
        self.load_clients()
        
        while True:
            self.username = input("enter username : ")

            if not v_username(self.username):
                print("> invalid username")
                
            else:
                print("> username valide ")
                break

        while True:
            self.password = input("enter password : ")

            if not v_password(self.password):
                print("> invalid password ")

            else:
                print("> password valide ")
                break
    
        for i in self.data_clients:
            if i["username"] == self.username and i["password"] == self.password:
                return Client(self.username, self.password)
                
        return False
    
    def register_client(self):

        while True:
            self.username = input("enter username : ")

            if not v_username(self.username):
                print("> invalid username")
                
            else:
                print("> username valide ")
                break

        while True:
            self.password = input("enter password : ")

            if not v_password(self.password):
                print("> invalid password ")

            else:
                print("> password valide ")
                break

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

            if not v_username(self.username):
                print("> invalid username")
                
            else:
                print("> username valide ")
                break

        while True:
            self.password = input("enter password : ")

            if not v_password(self.password):
                print("> invalid password ")

            else:
                print("> password valide ")
                break
        
        if self.username == "admin" and self.password == "admin":
            return Admin()