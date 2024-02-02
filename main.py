from manager import Manager
import sys

class Main():

    def __init__(self):
        self.manager = Manager()
        self.menu()

    def menu(self):
        print('\n')
        print("1. Afficher les produits")
        print("2. Ajouter un produit")
        print("3. Supprimer un produit")
        print("4. Modifier un produit")
        print("5. Quitter")
        User = input("Veuillez entrer votre choix :")

        try:
            choix = int(User)
        except ValueError:
            print("Choix. Veuillez entrer un nombre")
            self.menu()

        if choix == 1:
            self.readProduit()
        elif choix == 2:
            self.createProduct()
        elif choix == 3:
            self.deleteProduit()
        elif choix == 4:
            self.modifierProduit()
        elif choix == 5:
            sys.exit()
        else:
            print("Choix invalide")
            self.menu()

    def createProduct(self):
        name = input("Nom du produit : ")
        description = input("Description du produit : ")
        price = int(input("Prix du produit : "))
        quantity = int(input("Quantité de produit en stock : "))
        id_category = int(input("ID de la catégorie : "))

        # Appel de la méthode pour enregistrer le produit dans la base de données
        self.manager.createProduct(name, description, price, quantity, id_category)

        # Retour au menu principal
        self.menu()


    def readProduit(self):
        for produit in self.manager.readproduit():
            print("Produits : ")
            print(f"id : {produit[0]}")
            print(f"Nom : {produit[1]}")
            print(f"Description : {produit[2]}")
            print(f"Prix : {produit[3]}")
            print(f"Quantité : {produit[4]}")
            print(f"id_catégorie : {produit[5]}")
            print("------------------")
        self.menu()


    def modifierProduit(self):
        id_product = input("ID du produit à modifier : ")

        try:
            id_product = int(id_product)
        except ValueError:
            print("ID du produit invalide. Veuillez entrer un nombre.")
            self.menu()

    # Utilisez id_product ici pour éviter la confusion avec le nom
        name = input("Nouveau nom du produit : ")
        description = input("Nouvelle description du produit : ")
        price = int(input("Nouveau prix du produit : "))
        quantity = int(input("Nouvelle quantité de produit en stock : "))
        id_category = int(input("Nouvel ID de la catégorie : "))

        self.manager.modifierproduit(id_product, name, description, price, quantity, id_category)
        self.menu()


    def deleteProduit(self):
        id_product = int(input("Veuillez entrer l'ID du produit : "))

        try:
            id_product = (id_product)
        except ValueError:
            print("L'ID du produit est invalide. Veuillez entrer un nombre.")
            self.menu()

        self.manager.deleteproduit(id_product)
        self.menu()

Main()