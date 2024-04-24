# Ejercicio 4:
# Desarrolla una clase Cancion con los siguientes atributos:
# ● titulo: una variable String que guarda el título de la canción.
# ● autor: una variable String que guarda el autor de la canción.
# Con los siguientes métodos:
# ● Cancion(String, String): constructor que recibe como parámetros el título y el autor de la
# canción (por este orden).
# ● get_titulo(): devuelve el título de la canción.
# ● get_autor(): devuelve el autor de la canción.
# ● set_titulo(String): establece el título de la canción.
# ● set_autor(String): establece el autor de la canción

class Cancion:
    def __init__(self, titulo, autor):
        self._titulo = titulo
        self._autor = autor

    def __str__(self):  # ¡¡METODO ADICIONAL PARA PRUEBAS!!
        return f'''
Cancion: {self._titulo}
Artista: {self._autor}'''

    def get_titulo(self):
        return f'Titulo de la cancion: {self._titulo}'

    def get_autor(self):
        return f'Autor de la cancion: {self._autor}'

    def set_titulo(self, nuevoTitulo):
        self._titulo = nuevoTitulo
        return Cancion(self._titulo, self._autor)

    def set_autor(self, nuevoAutor):
        self._autor = nuevoAutor
        return Cancion(self._titulo, self._autor)


cancion1 = Cancion('Session en el barrio #5', 'Alejo Isakk')

print(cancion1.get_autor())
print(cancion1.get_titulo())

cancion1.set_autor('Callejero Fino')

print(cancion1.get_autor())
print(cancion1)