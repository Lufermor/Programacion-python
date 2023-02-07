class Vertex:
    '''Contiene una palabra y un diccionario de conexiones de esta, 
        este diccionario contiene las palabras conexiones junto con su peso'''

    def __init__(self, palabra:str):
        self.palabra = palabra
        self.connections = {}
        """ self.peso = 0 """

    def sumarPeso(self,palabra):
        """
        Comprueba si la palabra ya existe en las conexiones, 
        Si existe, aumenta su peso en uno, si no existe, añade un nuevo par 
        clave-valor al diccionario con un peso inicial de 1
        """
        if palabra in self.connections.keys(): self.connections[palabra] +=1
        else: self.connections[palabra] = 1