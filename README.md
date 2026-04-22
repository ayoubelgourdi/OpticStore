# Optic Store (CLI Project)

Simple command line application to manage an optic store.
The project is written in **Python** using **OOP (Object Oriented Programming)** and **JSON files** for data storage.

---

## Features

### Client

* Login
* Register
* Show products
* Add product to cart
* Remove product from cart
* Show cart
* Checkout

### Admin

* Login
* Add product
* Remove product
* Show products
* Update product stock
* Save products data

---

## Project Structure

```
OpticStore/
│
├── main.py
│
├── models/
│   ├── admin.py
│   ├── client.py
│   └── produit.py
│
├── services/
│   ├── auth.py
│   └── store.py
│
├── utils/
│   ├── menu.py
│   └── validation.py
│
├── data/
│   ├── clients.json
│   └── produits.json
│
└── README.md
```

---

## Installation

1. Clone the project

```bash
git clone https://github.com/ayoubelgourdi/OpticStore.git
```

2. Go to project folder

```bash
cd OpticStore
```

3. Run the program

```bash
python main.py
```

---

## Default Admin Account

```
username: admin
password: admin
```

---

## Data Storage

The project uses **JSON files** to store data.

* `clients.json` → stores registered clients
* `produits.json` → stores store products

Example product:

```json
{
  "modele": "RayBan",
  "couleur": "Black",
  "price": 120,
  "stock": 10
}
```

---

## Technologies Used

* Python
* Object Oriented Programming (OOP)
* JSON
* CLI (Command Line Interface)

---

## Author

Ayoub Elgourdi

---

## Future Improvements

* Product search
* Better error handling
* User interface
* Database integration
* Order history
