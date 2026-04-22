from services.auth import Auth
from services.store import Store
from utils.menu import menu

def main():

    auth = Auth()
    store = Store()

    store.load_products()

    menu_app = menu(store)

    while True:

        print("===== MAIN MENU =====")
        print("1 - Login Client")
        print("2 - Register Client")
        print("3 - Login Admin")
        print("4 - Exit")

        choice = input("> Choose option : ")

        if choice == "1":

            client = auth.login_client()

            if client:
                menu_app.client = client
                menu_app.menu_client()
            else:
                print("> Incorrect username or password")

        elif choice == "2":

            auth.register_client()
            print("> Client registered successfully")

        elif choice == "3":

            admin = auth.login_admin()

            if admin:
                admin.store = store
                menu_app.admin = admin
                menu_app.menu_admin()
            else:
                print("> Admin login failed")

        elif choice == "4":

            store.save_products()
            print("> Data saved")
            break

        else:
            print("> Invalid option")


main()