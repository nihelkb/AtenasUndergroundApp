import math as m

class parada:

#  Atributos
    id = 0
    nombre = ""
    longitud = 0
    latitud = 0
    conexiones = []
    coords = ()
    printCoords = ()
    color = ""

#  Constructor
    def __init__(self, id, nombre, longitud, latitud, coords, printCoords, color=None):
        self.id = id
        self.nombre = nombre
        self.longitud = longitud
        self.latitud = latitud
        self.conexiones = []
        self.coords = coords
        self.printCoords = printCoords
        self.color = color

    def __repr__(self):
        return self.nombre

#   Añade una conexion dada una parada y una distancia
    def añadirConexion(self, parada, distancia):
        self.conexiones.append((parada, distancia))

#  Comprueba que sus coordenadas esten en el circulo dado
    def is_in_circle (self, xp, yp):
        if self.coords == None:
            return False
        r = 15
        d = m.sqrt(pow(xp - self.coords[0],2) + pow((yp - self.coords[1]),2))
        if d <= r:
            return self
        else:
            return None