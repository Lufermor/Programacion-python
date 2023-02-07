import os

longitudes = []
ruta = "D:\Documentos\GradosuperiorDAM2021\Segundo-Curso\SGE\Python-workspace\Text_compositer\Lyrics"
newFile ="D:/Documentos/GradosuperiorDAM2021/Segundo-Curso/SGE/Python-workspace/Text_compositer/AllLyrics.txt"

with os.scandir(ruta) as ficheros:
    with open(newFile, 'w') as allLyrics:
        for fichero in ficheros:
            """ datos = fichero.read() """
            with open(fichero.path, 'r') as file:
                """ lon = 0 """
                file_string = file.read()
                
                file_string = file_string.replace(r"Ã¡","a")
                file_string = file_string.replace(r"Ãxa0","a")
                file_string = file_string.replace(r"Ã©","e")
                file_string = file_string.replace(r"Ã¨","e")
                file_string = file_string.replace(r"Ãxad","i")
                file_string = file_string.replace(r"Ã\xad","i")
                file_string = file_string.replace(r"Ã¬","i")
                file_string = file_string.replace(r"ã\\xad","i")
                file_string = file_string.replace(r"ã\xad","i")
                file_string = file_string.replace(r"ãxad","i")
                file_string = file_string.replace(r"Ã\\xad","i")
                file_string = file_string.replace(r"Ã³","o")
                file_string = file_string.replace(r"Ã²","o")
                file_string = file_string.replace(r"ã³","o")
                file_string = file_string.replace(r"Ãº","u")
                file_string = file_string.replace(r"Ã¼","u")
                file_string = file_string.replace(r"Ã±","ny")
                file_string = file_string.replace(r"Ã§","c")

                file_string = file_string.replace(r"Ã‰","E")
                file_string = file_string.replace(r"Ã“","O")
                file_string = file_string.replace(r"Ã’","O")
                file_string = file_string.replace(r"Ãš","U")
                file_string = file_string.replace(r"Ã‘","NY")
                file_string = file_string.replace(r"Ã‡","C")
                """
                Hay una palabra con tilde que se resiste a ser reemplazada, así que vamos a 
                aislar el problema y a reemplazarlo de forma interna para deshacernos de esa
                tilde.
                """
                problema = ""
                with open('D:/Documentos/GradosuperiorDAM2021/Segundo-Curso/SGE/Python-workspace/Text_compositer/a.txt', 'r') as f:
                    problema = f.readline().split()[2].replace('a', '').replace('q', '').replace('u', '')
                file_string = file_string.replace(problema,"i")
                # A continuación quitamos los signos de puntuación que se han visto en los documentos
                file_string = file_string.replace(r",","").replace(".","").replace(r"!","").replace("\"","")
                file_string = file_string.lower()
                print(file_string)
                palabras = file_string.split()
                print(palabras)
                longitudes.append(len(palabras))
                allLyrics.write(file_string)
                #El archivo acaba con 795 filas
            allLyrics.write("\n\n\n")
            #El archivo acaba con 855 líneas
            
print(len(longitudes))
print(longitudes)
print(max(longitudes))