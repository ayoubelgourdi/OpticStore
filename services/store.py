from models.produit import Produit
import json

class Store:
    def __init__(self,):
        self.products = []
        self.clients = []

    def check_list(self):
        if not self.products:
            print("> No products available in the store")
            return True


    def add_product(self,product):
        self.products.append(product)

    def show_products(self):
        if self.check_list() == True:
            return "> No products available in the store"
        
        for i in self.products:
            print(i.get_produit())
        
    def delete_product(self,indix):
        self.show_products()

        self.products.pop(indix)

    def find_product_by_modele(self,modele):
        self.check_list()

        for i in self.products:
            if modele == i.modele:
                return i.get_produit()
            
        return f"> product not found :("
        
    def sell_product(self,modele,quantity):
        for i in self.products:
            if i.modele  == modele.upper():
                i.remove_stock(quantity)
                return True

        return False
        

    def load_products(self):
        try:
            with open("/home/ayoub/OpticStore/data/produits.json","r") as F:
                self.data = json.load(F)

            self.products = []

            for i in self.data:
                self.products.append(Produit(
                    i["modele"],
                    i["couleur"],
                    i["price"],
                    i["stock"]
                ))
            return "> products loaded successfully"

        except FileNotFoundError:
            return "> products file not found"
        
    def save_products(self):
        self.products_data = []

        for i in self.products:
            p_dict = {
                "modele": i.modele,
                "couleur": i.couleur,
                "price": i.price,
                "stock": i.get_stock()
            }

            self.products_data.append(p_dict)

        with open("/home/ayoub/OpticStore/data/produits.json","w") as F:
            json.dump(self.products_data, F, indent=4)

    def update_stock(self,modele, quantity):
        for i in self.products:
            if i.modele == modele:
                while True:
                    print("===menu===")
                    print("1 - add")
                    print("2 - remove")

                    choose = input("enter choose : ")

                    if choose == "1":
                        i.add_stock(quantity)
                        return "> stock updated"
                        

                    elif choose == "2":
                        i.remove_stock(quantity)
                        return "> stock updated"

        
        return "> product not found"

