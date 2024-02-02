from database import Database

class Product:
    def __init__(self):
        self.table = 'product'
        self.database = Database(host='localhost', user='root', password='root', database='store')


    def Create(self, name, description, price, quantity, id_category):
        query = f'INSERT INTO {self.table} (name, description, price, quantity, id_category) VALUES (%s, %s, %s, %s, %s)'
        params = (name, description, price, quantity, id_category)
        self.database.executeQuery(query, params)


    def Read(self):
        query = f'SELECT * FROM {self.table}'
        return self.database.fetch(query)

    def Delete(self, id_product):
        query = f'DELETE FROM {self.table} WHERE id=%s'
        params = (int(id_product),)
        self.database.executeQuery(query, params)

    def Modifier(self, id, name, description, price, quantity, id_category):
        query = f'UPDATE {self.table} SET name=%s, description=%s, price=%s, quantity=%s, id_category=%s WHERE id=%s'
        params = (name, description, price, quantity, id_category, id)
        self.database.executeQuery(query, params)