import BaseDatos
import mysql


class MySQL(BaseDatos):
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None
    
    def conectar(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
    
    def desconectar(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
    
    def ejecutar_query(self, query, data=None):
        try:
            self.conectar()
            if data:
                self.cursor.execute(query, data)
            else:
                self.cursor.execute(query)
            self.connection.commit()
        except Exception as e:
            print(f"Error al ejecutar la consulta: {e}")
            self.connection.rollback()
        finally:
            self.desconectar()