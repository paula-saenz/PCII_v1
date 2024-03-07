import DatabaseManager

class DBHelper:
    def __init__(self):
        self.db_manager = DatabaseManager(host='93.93.118.169', user='baboo', password='baboo2024', database='baboo_manager')

    # Función para realizar una consulta SELECT
    def select_query(self, query, data=None):
        return self.db_manager.select(query, data)

    # Función para realizar una consulta INSERT
    def insert_query(self, query, data):
        self.db_manager.insert(query, data)

    # Función para realizar una consulta UPDATE
    def update_query(self, query, data):
        self.db_manager.update(query, data)

    # Función para realizar una consulta DELETE
    def delete_query(self, query, data=None):
        self.db_manager.delete(query, data)
