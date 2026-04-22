from services.store import Store

class Admin:

    def __init__(self):

        self.__usernam = "admin"
        self.__password = "admin"
        self.store = None


    def admin_login(self,usernam,pasword):

        if usernam == self.__usernam and pasword == self.__password:
            return True
        else:
            return False


    def add_product(self,modele,couleur,price,stock):

        self.store.add_product(modele,couleur,price,stock)


    def remove_product(self,indix):

        self.store.delete_product(indix)


    def update_stock(self,modele,quantity):

        self.store.sell_product(modele,quantity)