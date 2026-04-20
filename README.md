ndir login :
    admin -> user admin - pasword admin - numbeer de tele : admin
    client -> user w password w number de tele

    andir ila kan user admin iktb nichan menu dyal admine bla mayswl baqi 
    w cleint la iswlo 


admin :
    <!-- >> 1 ajouter (modele - couleur - price - stock) -->
    <!-- >> 2 ibdl price  -->
    <!-- >> 2 izid f stock -->
    <!-- >> 3 afficher stock (modele - couleur - price - stock) -->
    >> 4 afficher commands (client name - produit(modele - couleur) - number de tele - price - date - wchhal b9a bach tms7 - id)
    >> 5 supprimer commandes (outomatique b3d chhr - wla b id)
    >> 6 statistique (trtib dyal modele li tba3o aktar l a9al wahd + total d flous d kola modele 
    w flt7t total dyal lmabi3at ) (kola chher kat3awd outomatique)

    ichof stock li tsalaw




cleint :
    >> afficher ga3 le modile li kaynin blwan dyalhom w price 
    (ikhtar wla search )
        >> search 3la chi modile wach kayn (wach khtar dak modele wla al )
    >> ikhtar coulor mn coulors li mtwfriin f dak modele (irj3 lor)
    >> ichof commande (modele - colour - price )( ikml tla7 f sla wla panier - exit - irj3 lor ) (ila kml (wach izid command khra wla i7bs))
    >> f meni : sla wla panier ichofha w modifer fchi commande + idwz commands (it3taha id outomatique)
    

    stock = stock - quantité






    structure :
                OpticStore
                ├── README.md
                ├── data
                │   └── produits.json
                ├── main.py
                ├── models
                │   ├── admin.py
                │   ├── client.py
                │   └── produit.py
                ├── services
                │   ├── auth.py
                │   └── store.py
                └── utils
                    └── menu.py


                
        main.py
        |
        |---- menu
        |
        |---- auth
        |
        |---- store
                |
                |---- models (Produit / Client)
                |
                |---- data (json)



mansach nbdl lpath d open files 