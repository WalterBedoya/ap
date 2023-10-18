from dataclasses import dataclass

@dataclass
class Elemento:
    nombre: str

    def __eq__(self, other):
        return self.nombre == other.nombre

@dataclass
class Conjunto:
    contador = 0

    def __init__(self, nombre, elementos=None):
        self.elementos = elementos if elementos is not None else []
        self.nombre = nombre
        self.__id = Conjunto.contador
        Conjunto.contador += 1

    @property
    def id(self):
        return self.__id

    def contiene(self, elemento):
        return any(e == elemento for e in self.elementos)

    def agregar_elemento(self, elemento):
        if not self.contiene(elemento):
            self.elementos.append(elemento)

    def __add__(self, other):
        nuevo_nombre = f"{self.nombre} UNIDO {other.nombre}"
        elementos_unidos = self.elementos + [elemento for elemento in other.elementos if elemento not in self.elementos]
        return Conjunto(nuevo_nombre, elementos_unidos)

    @classmethod
    def intersectar(cls, conjunto1, conjunto2):
        elementos_comunes = [elemento for elemento in conjunto1.elementos if elemento in conjunto2.elementos]
        nuevo_nombre = f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}"
        return Conjunto(nuevo_nombre, elementos_comunes)

    def __str__(self):
        elementos_str = ", ".join(e.nombre for e in self.elementos)
        return f"Conjunto {self.nombre}: ({elementos_str})"