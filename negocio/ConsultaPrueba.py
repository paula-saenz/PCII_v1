from persistencia.DatabaseManager import DatabaseManager

class ConsultaPrueba:
    def __init__(self):
        self.db_manager = DatabaseManager(
            host='93.93.118.169', 
            user='baboo', 
            password='baboo2024', 
            database='baboo_manager'
        )

    def obtener_jugadores_por_nacionalidad(self, nacionalidad):
        jugadores = self.db_manager.select_jugadores_by_nationality(nacionalidad)
        return jugadores
