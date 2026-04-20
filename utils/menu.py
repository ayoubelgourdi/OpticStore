from utils.menu import Auth
from services.store import Store
from models.produit import Produit
from models.client import Client
from utils.validation import v_price
from utils.validation import v_quantity

class menu:
    def menu_principal(self):
        while True:
            print("===== OPTIC STORE =====")
            print("1 - Login Client")
            print("2 - Register Client")
            print("3 - Login Admin")
            print("4 - Exit")
            choose = input("> Choose option : ")

            if choose == "1":
                self.login_client()

            elif choose == "2":
                self.register_client()

            elif choose == "3":
                self.login_admin()

            elif choose == "4":
                break
            
            else:
                print("choose not valide !")
        
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
                modele = input("enter modele : ")
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

                object = Produit(modele,couleur,price,stock)
                self.add_product(object)

            elif choose == "2":
                self.show_products()

                self.save_products()
            elif choose == "3":
                self.show_products()
                index = int(input("enter index : "))

                self.delete_product(index)
                
                self.save_products()
            elif choose == "4":
                self.show_products()
                modele = input("enter modele")
                while True:
                    quantity = int(input("enter quantity : "))
                    if not v_quantity(quantity):
                        print("> invalide quantity ")
                    else:
                        break

                self.update_stock(modele, quantity)

                self.save_products()
            elif choose == "5":
                self.save_products()
                
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

            if choose =="1":
                self.show_products()

            elif choose == "2":
                modele = input("enter modele : ")

                while True:
                    quantity = int(input("enter quantity : "))
                    if not v_quantity(quantity):
                        print("> invalide quantity ")
                    else:
                        break

                    for i in self.store.products:
                        if i.modele == modele:
                            self.add_to_cart(i,quantity)

            elif choose == "3":
                self.show_cart()
            
            elif choose == "4":
                self.show_cart()

                index = int(input("enter index : "))
                self.remove_from_cart(index)

            elif choose == "5":
                self.checkout()

            elif choose == "6":
                break
            
