from models.produit import Produit

class Client:
    def __init__(self,usernam,password):
        self.usernam = usernam
        self.__password = password
        self.panier = []

    def add_to_cart(self,produit,quantity):
        self.panier.append((produit,quantity))

    def remove_from_cart(self,indix):
        
        self.panier.pop(indix)

    def show_cart(self):
        if not self.panier:
            return f"> ur cart is empty :( Add products to continue"
        
        a = 0
        for produit,quantity in self.panier:
            print(f"{a} | {produit.get_produit()} | qty : {quantity}")
            a += 1

    def checkout(self):
        if not self.panier:
            return f"> ur cart is empty :( Add products to continue"
        
        self.show_cart()
        
        total = 0
        for produit,quantity in self.panier:
            if not produit.can_sell(quantity):
                return f"> not enough stock for {produit.modele}"

        for produit,quantity in self.panier:
            total += produit.price * quantity
            produit.remove_stock(quantity)

        self.panier.clear()

        return f"> Purchase successful \n> TOTAL : {total}"