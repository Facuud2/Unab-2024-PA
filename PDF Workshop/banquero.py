from trabajador import Trabajador

class Banquero(Trabajador):
    def __init__(self, nombre, edad, sexo, dni, id, sueldo, turno, cargo):
        super().__init__(nombre, edad, sexo, dni, 'Banquero', 'Finanzas', id, sueldo, turno)
        self._cargo = cargo

    def carnetLaboral(self):
        print(f'''
Carnet laboral: 
ID: {self._id}
Sueldo: ${self._sueldo}
Turno: {self._turno}
Importancia: {self._cargo}''')

banquero1 = Banquero('Florencia Marquez', 37, 'F', 27464211, 'F41V', 350000, 'Mañana', 'Jefe de personal')

