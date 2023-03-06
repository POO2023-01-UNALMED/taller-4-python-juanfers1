class Asignatura:

    def __init__(self, nombre, salon="remoto"):
        self._nombre = nombre
        self._salon = salon

    # Este metodo es para imprimir el nombre y el salon de la asignatura 
    def __str__(self):
        string= self._nombre + " " + self._salon
        return string
