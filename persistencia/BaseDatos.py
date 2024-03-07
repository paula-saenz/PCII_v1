from abc import ABC, abstractmethod

class BaseDatos(ABC):
    @abstractmethod
    def conectar(self):
        pass
    
    @abstractmethod
    def desconectar(self):
        pass
    
    @abstractmethod
    def ejecutar_query(self, query, data=None):
        pass