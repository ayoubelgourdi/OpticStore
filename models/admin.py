class Admin:
    def __init__(self):
        self.__usernam = "admin"
        self.__password = "admin"
    
    def admin_login(self,usernam,pasword):
        if usernam == self.__usernam and pasword == self.__password:
            return True
        else:
            return False
        
    def add_product(self,modele,couleur,price,stock):
        # store.add_product()
        ...

    def remove_product(self):
        # store.add_product()
        ...

    def update_stock(self):
        # store.update_stock()
        ...

    