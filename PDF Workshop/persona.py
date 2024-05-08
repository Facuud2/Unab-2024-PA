class Persona:
    """ Clase padre con asignacion de atributos a una persona """
    def __init__(self, nombre, edad, sexo, dni, ocupacion):
        self._nombre = nombre
        self._edad = edad
        self._sexo = sexo
        self._dni = dni
        self._ocupacion = ocupacion

    def __str__(self):
        return f'''
Identidad Nacional:
Nombre: {self._nombre}
Edad: {self._edad}
Sexo: {self._sexo}
DNI: {self._dni}
Ocupacion: {self._ocupacion}'''