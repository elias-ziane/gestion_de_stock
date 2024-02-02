from product import Product
from database import Database

class Manager:

    def __init__(self) -> None:
        self.product = Product()     
        

    def createProduct(self, name, description, price, quantity, id_category):
        self.product.Create(name, description, price, quantity, id_category)

    def readproduit(self):
        return self.product.Read()
    
    def modifierproduit(self, id, name, description, price, quantity, id_category):
        self.product.Modifier(id, name, description, price, quantity, id_category)
    
    def deleteproduit(self, id):
        self.product.Delete(id)