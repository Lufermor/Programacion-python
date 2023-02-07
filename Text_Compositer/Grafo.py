class Graph:
    """
    Clase que almacena una lista de vertex.
    También contiene un método para realizar la limpieza de 
    una cadena que se le pase 
    """
    
    def __init__(self): 
        self.listaVertex = []
        self.longitudCanciones = []

    def addVertex(self,vertex):
        '''Agrega el vertex que se le pasa a la lista.'''
        self.listaVertex.append(vertex)
    
    def palabraEnLista(self, newVertex):
        '''Comprueba si la palabra que se le pasa ya está en alguno 
            de los vertex de la lista'''
        if not self.listaVertex:
            return False
        for vertex in self.listaVertex:
            if vertex.palabra == newVertex.palabra: 
                newVertex.connections = vertex.connections
                return True
        return False

    def getVertex(self, word):
        '''
        Comprueba que la lista de vertex no esté vacía, a continuación
        comprueba si la palabra ya está en alguno de los vertex de la lista
        en caso positivo, devuelve el vertex correspondiente,
        si no hay ningún vertex con esa palabra, devuelve None.
        '''
        if len(self.listaVertex) == 0:
            return None
        for vertex in self.listaVertex:
            if vertex.palabra == word: 
                return vertex
        return None
    
    def limpiarCadena(self, cadena):
        """
        Recibe un string que puede contener muchas palabras,
        entonces realiza operaciones de limpieza para eliminar tildes,
        signos de puntuación y caracteres extraños.
        Crea una lista con las palabras de la cadena y añade la longitud 
        de esta lista a self.longitudCanciones
        Por último devuelve la lista con las palabras de la cadena.
        """
        cadena = cadena.replace(r"Ã¡","a")
        cadena = cadena.replace(r"Ãxa0","a")
        cadena = cadena.replace(r"Ã©","e")
        cadena = cadena.replace(r"Ã¨","e")
        cadena = cadena.replace(r"Ãxad","i")
        cadena = cadena.replace(r"Ã\xad","i")
        cadena = cadena.replace(r"Ã¬","i")
        cadena = cadena.replace(r"ã\\xad","i")
        cadena = cadena.replace(r"ã\xad","i")
        cadena = cadena.replace(r"ãxad","i")
        cadena = cadena.replace(r"Ã\\xad","i")
        cadena = cadena.replace(r"Ã³","o")
        cadena = cadena.replace(r"Ã²","o")
        cadena = cadena.replace(r"ã³","o")
        cadena = cadena.replace(r"Ãº","u")
        cadena = cadena.replace(r"Ã¼","u")
        cadena = cadena.replace(r"Ã±","ny")
        cadena = cadena.replace(r"Ã§","c")

        cadena = cadena.replace(r"Ã‰","E")
        cadena = cadena.replace(r"Ã“","O")
        cadena = cadena.replace(r"Ã’","O")
        cadena = cadena.replace(r"Ãš","U")
        cadena = cadena.replace(r"Ã‘","NY")
        cadena = cadena.replace(r"Ã‡","C")
        """
        Hay una palabra con tilde que se resiste a ser reemplazada, así que vamos a 
        aislar el problema y a reemplazarlo de forma interna para deshacernos de esa
        tilde.
        """
        problema = ""
        with open('D:/Documentos/GradosuperiorDAM2021/Segundo-Curso/SGE/Python-workspace/Text_compositer/a.txt', 'r') as f:
            problema = f.readline().split()[2].replace('a', '').replace('q', '').replace('u', '')
        cadena = cadena.replace(problema,"i")
        # A continuación quitamos los signos de puntuación que se han visto en los documentos
        cadena = cadena.replace(r",","").replace(".","").replace(r"!","").replace("\"","")
        cadena = cadena.lower()
        palabras = cadena.split()
        self.longitudCanciones.append(len(palabras))
        return palabras