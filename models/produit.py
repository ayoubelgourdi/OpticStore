class Produit:
    def __init__(self,modele,couleur,price,stock):
        self.modele = modele
        self.couleur = couleur
        self.price = price
        self.__stock = stock
        
    def get_produit(self):
        return f"> Modele : {self.modele} | Couleur : {self.couleur} | Price : {self.price}"
    
    def remove_stock(self,quantity):
        if self.can_sell(quantity) == True:
            self.__stock -= quantity
            return True
        else:
            print("> not enough stock :(")
            return False

    def add_stocj(self,quantity):
        self.__stock += quantity

    def can_sell(self,quantity):
        if quantity <= self.__stock:
            return True
        else:
            return False
        