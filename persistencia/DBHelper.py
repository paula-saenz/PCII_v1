import DatabaseManager


class DBHelper:
    def __init__(self, query, data):
        self.db_manager = DatabaseManager(
            host='93.93.118.169', user='baboo', password='baboo2024', database='baboo_manager')
        self.__query = query
        self.__data = data

    # Función para realizar una consulta SELECT
    def select_query(self):
        return self.db_manager.select(self.__query, self.__data)

    # Función para realizar una consulta INSERT
    def insert_query(self):
        self.db_manager.insert(self.__query, self.__data)

    # Función para realizar una consulta UPDATE
    def update_query(self):
        self.db_manager.update(self.__query, self.__data)

    # Función para realizar una consulta DELETE
    def delete_query(self):
        self.db_manager.delete(self.__query, self.__data)
