import os
import random
from Grafo import Graph
from Vertex import Vertex

#Ruta donde se encuentran los ficheros con las lyrics
ruta = "D:/Documentos/GradosuperiorDAM2021/Segundo-Curso/SGE/Python-workspace/Text_compositer/Lyrics"
graph = Graph()

def read_text_file(file_path):
    """
    Este método recibe la ruta a un fichero, lo abre y guarda sus palabras
    en una lista. 
    A continuación recorre la lista y crea vertex con estas
    palabras, comprueba si estos vertex ya existen en el grafo, 
    si ya existen, entonces toma el vertex existente, sino, añade el 
    nuevo vertex al grafo.
    Luego, si la palabra no es la primera del fichero, aumenta el peso
    de dicha palabra en el vertex de la palabra anterior.
    """
    anterior = None
    newVertex = None
    palabras = []

    with open(file_path, 'r') as file:
        palabras = graph.limpiarCadena(file.read())
    
    for palabra in palabras:
        newVertex = Vertex(palabra)
        if not graph.palabraEnLista(newVertex):
            graph.addVertex(newVertex)
        #else:

        if anterior is not None:
            anterior.sumarPeso(palabra)
        anterior = newVertex

def crear_grafo():
    """
    Con la ruta establecida al inicio del fichero, obtiene los ficheros 
    txt de esa ruta, y se los envía al método read_text_file para leer cada uno
    e ir creando el grafo 
    """
    with os.scandir(ruta) as ficheros:
        for fichero in ficheros:
            if fichero.name.endswith(".txt"): 
                read_text_file(fichero.path)

""" print(v.palabra for v in graph.listaVertex) """#No sé por qué esto no funciona
def mostrar_vertex_grafo():
    """
    Recorre la lista de vertex en el grafo e imprime por pantalla
    la palabra de cada vertex junto a su número de conexiones.
    """
    for vert in graph.listaVertex:
        print(vert.palabra, len(vert.connections.keys()))

def crear_cancion():
    """
    Escoge una longitud de palabras aleatorias, empieza con la palabra
    de un vertex aleatorio del grafo, a continuación, busca dentro de la 
    lista de conexiones del vertex, para escoger de forma semialeatoria, 
    influenciado por su peso, la siguiente palabra de la canción,
    continúa escogiendo palabras hasta que ha llegado a la longitud determinada 
    y guarda la cadena resultante en un fichero.
    """
    lenCancion = random.randint(min(graph.longitudCanciones), max(graph.longitudCanciones))
    print(f"\t  Longitud de la nueva canción = {lenCancion}")
    vertexActual = graph.listaVertex[random.randint(0,len(graph.listaVertex))]
    print(f"Palabra inicial : {vertexActual.palabra}")
    cancion = vertexActual.palabra
    for i in range(lenCancion):
        nextWord = random.choices(list(vertexActual.connections.keys()), 
            weights = list(vertexActual.connections.values()), k = 1)[0]
        cancion += " " + nextWord
        vertexActual = graph.getVertex(nextWord)
        #graph.palabraEnLista(vertexActual)
    print(f"La nueva canción queda así: \n{cancion}")
    newFile ="D:/Documentos/GradosuperiorDAM2021/Segundo-Curso/SGE/Python-workspace/Text_compositer/NuevaCancion.txt"
    with open(newFile, 'w') as nuevaCancion:
        nuevaCancion.write(cancion)

#Ahora ejecutamos el programa:
crear_grafo()
#mostrar_vertex_grafo()
print(graph.getVertex("llanto").connections)
crear_cancion()