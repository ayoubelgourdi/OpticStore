from services.auth import Auth
from services.store import Store
from models.produit import Produit
from models.client import Client
from utils.validation import v_price
from utils.validation import v_quantity


class menu:

    def __init__(self, store):
        self.store = store
        self.client = None
        self.admin = None


    def menu_admin(self):

        while True:

            print("===== ADMIN MENU =====")
            print("1 - Add product")
            print("2 - Show products")
            print("3 - Remove product")
            print("4 - Update stock")
            print("5 - Save data")
            print("6 - Logout")

            choose = input("> Choose option : ")

            if choose == "1":

                modele = input("enter modele : ").upper()
                couleur = input("enter couleur : ")

                while True:

                    price = input("enter price : ")

                    if not v_price(price):
                        print("> invalide price ")
                    else:
                        break

                while True:

                    stock = input("enter stock : ")

                    if not v_quantity(stock):
                        print("> invalide stock")
                    else:
                        break

                product = Produit(modele, couleur, float(price), int(stock))

                self.store.add_product(product)


            elif choose == "2":

                self.store.show_products()


            elif choose == "3":

                self.store.show_products()

                indix = int(input("enter index : "))

                self.store.delete_product(indix)


            elif choose == "4":

                self.store.show_products()

                modele = input("enter modele : ").upper()

                while True:

                    quantity = input("enter quantity : ")

                    if not v_quantity(quantity):
                        print("> invalide quantity ")
                    else:
                        break

                self.store.update_stock(modele, int(quantity))


            elif choose == "5":

                self.store.save_products()


            elif choose == "6":

                break



    def menu_client(self):

        while True:

            print("===== CLIENT MENU =====")
            print("1 - Show Products")
            print("2 - Add Product To Cart")
            print("3 - Show Cart")
            print("4 - Remove From Cart")
            print("5 - Checkout")
            print("6 - Logout")

            choose = input("> Choose option : ")

            if choose == "1":

                self.store.show_products()


            elif choose == "2":

                modele = input("enter modele : ").upper()

                while True:

                    quantity = input("enter quantity : ")

                    if not v_quantity(quantity):
                        print("> invalide quantity ")
                    else:
                        break

                quantity = int(quantity)

                for i in self.store.products:

                    if i.modele == modele:
                        self.client.add_to_cart(i, quantity)


            elif choose == "3":

                print(self.client.show_cart())


            elif choose == "4":

                self.client.show_cart()

                indix = int(input("enter index : "))

                self.client.remove_from_cart(indix)


            elif choose == "5":

                print(self.client.checkout())
                self.store.save_products()


            elif choose == "6":

                break