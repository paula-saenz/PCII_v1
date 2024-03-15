from abc import ABC, abstractmethod


class BaseDatos(ABC):
    @abstractmethod
    def conectar(self):
        pass

    @abstractmethod
    def desconectar(self):
        pass

    @abstractmethod
    def insertar(self, query, data):
        pass

    @abstractmethod
    def actualizar(self, query, data):
        pass

    @abstractmethod
    def eliminar(self, query, data):
        pass

    @abstractmethod
    def seleccionar(self, query, data):
        pass
