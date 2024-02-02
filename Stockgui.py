import tkinter as tk
from manager import Manager

class StockGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Gestion de Stock")
        self.root.geometry("800x600")  # Ajustez la taille de la fenêtre principale selon vos préférences
        self.root.configure(bg="#f0f0f0")  # Fond gris clair

        self.manager = Manager()

        # Créez les widgets
        self.label = tk.Label(self.root, text="Bienvenue dans le gestionnaire de stock", font=("Helvetica", 16), bg="#f0f0f0", fg="black")
        self.label.pack(pady=20)

        button_config = {"bg": "#d9d9d9", "fg": "black", "padx": 20, "pady": 10, "font": ("Helvetica", 12)}

        self.btn_afficher = tk.Button(self.root, text="Afficher les produits", command=self.afficher_produits, **button_config)
        self.btn_afficher.pack(pady=10)

        self.btn_ajouter = tk.Button(self.root, text="Ajouter un produit", command=self.ajouter_produit, **button_config)
        self.btn_ajouter.pack(pady=10)

        self.btn_supprimer = tk.Button(self.root, text="Supprimer un produit", command=self.supprimer_produit, **button_config)
        self.btn_supprimer.pack(pady=10)

        self.btn_modifier = tk.Button(self.root, text="Modifier un produit", command=self.modifier_produit, **button_config)
        self.btn_modifier.pack(pady=10)

        self.btn_quitter = tk.Button(self.root, text="Quitter", command=self.root.destroy, **button_config)
        self.btn_quitter.pack(pady=20)

        self.root.mainloop()

    def afficher_produits(self):
        produits = self.manager.readproduit()

        # Créez une nouvelle fenêtre pour afficher les produits
        display_window = tk.Toplevel(self.root)
        self.setup_display_window(display_window)

        text_widget = tk.Text(display_window, height=20, width=80, wrap=tk.WORD)
        text_widget.pack(expand=True, fill=tk.BOTH)

        if produits:
            for produit in produits:
                text_widget.insert(tk.END, "Produits :\n")
                text_widget.insert(tk.END, f"id : {produit[0]}\n")
                text_widget.insert(tk.END, f"Nom : {produit[1]}\n")
                text_widget.insert(tk.END, f"Description : {produit[2]}\n")
                text_widget.insert(tk.END, f"Prix : {produit[3]}\n")
                text_widget.insert(tk.END, f"Quantité : {produit[4]}\n")
                text_widget.insert(tk.END, f"id_catégorie : {produit[5]}\n")
                text_widget.insert(tk.END, "------------------\n")
        else:
            text_widget.insert(tk.END, "Aucun produit disponible.\n")

    def setup_display_window(self, window):
        window.title("Afficher les produits")
        window.geometry("800x600")  # Ajustez la taille de la fenêtre selon vos préférences
        window.configure(bg="#f0f0f0")  # Fond gris clair

    def ajouter_produit(self):
        # Fonction pour ajouter le produit
        def add_product():
            name = name_entry.get()
            description = description_entry.get()
            price = int(price_entry.get())
            quantity = int(quantity_entry.get())
            id_category = int(id_category_entry.get())

            self.manager.createProduct(name, description, price, quantity, id_category)
            add_window.destroy()

        # Créez une fenêtre pour ajouter un produit
        add_window = tk.Toplevel(self.root)
        self.setup_window(add_window, "Ajouter un produit", height=500, width=400)

        # Créez les champs de saisie
        tk.Label(add_window, text="Nom du produit :", bg="#f0f0f0", fg="black").pack(pady=5)
        name_entry = tk.Entry(add_window)
        name_entry.pack(pady=5)

        tk.Label(add_window, text="Description du produit :", bg="#f0f0f0", fg="black").pack(pady=5)
        description_entry = tk.Entry(add_window)
        description_entry.pack(pady=5)

        tk.Label(add_window, text="Prix du produit :", bg="#f0f0f0", fg="black").pack(pady=5)
        price_entry = tk.Entry(add_window)
        price_entry.pack(pady=5)

        tk.Label(add_window, text="Quantité de produit en stock :", bg="#f0f0f0", fg="black").pack(pady=5)
        quantity_entry = tk.Entry(add_window)
        quantity_entry.pack(pady=5)

        tk.Label(add_window, text="ID de la catégorie :", bg="#f0f0f0", fg="black").pack(pady=5)
        id_category_entry = tk.Entry(add_window)
        id_category_entry.pack(pady=5)

        # Bouton pour ajouter le produit
        add_button = tk.Button(add_window, text="Ajouter", command=add_product, bg="#d9d9d9", fg="black", padx=20, pady=10, font=("Helvetica", 12))
        add_button.pack(pady=10)

    def supprimer_produit(self):
        # Fonction pour supprimer le produit
        def delete_product():
            id_product = int(id_product_entry.get())
            self.manager.deleteproduit(id_product)
            delete_window.destroy()

        # Créez une fenêtre pour supprimer un produit
        delete_window = tk.Toplevel(self.root)
        self.setup_window(delete_window, "Supprimer un produit", height=150, width=250)  # Ajustez les dimensions ici

        tk.Label(delete_window, text="ID du produit à supprimer :", bg="#f0f0f0", fg="black").pack(pady=5)
        id_product_entry = tk.Entry(delete_window)
        id_product_entry.pack(pady=5)

        # Bouton pour supprimer le produit
        delete_button = tk.Button(delete_window, text="Supprimer", command=delete_product, bg="#d9d9d9", fg="black", padx=20, pady=10, font=("Helvetica", 12))
        delete_button.pack(pady=10)

    def modifier_produit(self):
        # Fonction pour modifier le produit
        def modify_product():
            id_product = int(id_product_entry.get())
            name = name_entry.get()
            description = description_entry.get()
            price = int(price_entry.get())
            quantity = int(quantity_entry.get())
            id_category = int(id_category_entry.get())

            self.manager.modifierproduit(id_product, name, description, price, quantity, id_category)
            modify_window.destroy()

        # Créez une fenêtre pour modifier un produit
        modify_window = tk.Toplevel(self.root)
        self.setup_window(modify_window, "Modifier un produit", height=500, width=400)

        tk.Label(modify_window, text="ID du produit à modifier :", bg="#f0f0f0", fg="black").pack(pady=5)
        id_product_entry = tk.Entry(modify_window)
        id_product_entry.pack(pady=5)

        tk.Label(modify_window, text="Nouveau nom du produit :", bg="#f0f0f0", fg="black").pack(pady=5)
        name_entry = tk.Entry(modify_window)
        name_entry.pack(pady=5)

        tk.Label(modify_window, text="Nouvelle description du produit :", bg="#f0f0f0", fg="black").pack(pady=5)
        description_entry = tk.Entry(modify_window)
        description_entry.pack(pady=5)

        tk.Label(modify_window, text="Nouveau prix du produit :", bg="#f0f0f0", fg="black").pack(pady=5)
        price_entry = tk.Entry(modify_window)
        price_entry.pack(pady=5)

        tk.Label(modify_window, text="Nouvelle quantité de produit en stock :", bg="#f0f0f0", fg="black").pack(pady=5)
        quantity_entry = tk.Entry(modify_window)
        quantity_entry.pack(pady=5)

        tk.Label(modify_window, text="Nouvel ID de la catégorie :", bg="#f0f0f0", fg="black").pack(pady=5)
        id_category_entry = tk.Entry(modify_window)
        id_category_entry.pack(pady=5)

        # Bouton pour modifier le produit
        modify_button = tk.Button(modify_window, text="Modifier", command=modify_product, bg="#d9d9d9", fg="black", padx=20, pady=10, font=("Helvetica", 12))
        modify_button.pack(pady=10)

    def setup_window(self, window, title, height=None, width=None):
        window.title(title)
        if height and width:
            window.geometry(f"{width}x{height}")
        window.configure(bg="#f0f0f0")  # Fond gris clair

# Initialisez l'interface graphique
if __name__ == "__main__":
    StockGUI()
