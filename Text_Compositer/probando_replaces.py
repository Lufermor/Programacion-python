import random

s = 'tãº y tãº y tãº'
print(s.replace("tãº", "tu"))

problema = ""
with open('D:/Documentos/GradosuperiorDAM2021/Segundo-Curso/SGE/Python-workspace/Text_compositer/a.txt', 'r') as f:
    problema = f.readline().split()[2].replace('a', '').replace('q', '').replace('u', '')
#palabras = linea.split()
#problema = palabras[2].replace('a', '').replace('q', '').replace('u', '')
print(problema)
""" solucion = palabras[2].replace(problema, 'i')
print(solucion) """

mydict = {"a": 1}
mydict['a'] += 1
print(mydict)
mydict['b'] = 1
print(mydict)
print(len(mydict.keys()))
print(len(mydict.values()))
print(len(mydict))
print(min(mydict.values()))
mydict['c'] = 60
mydict['d'] = 40
mydict['e'] = -5
print(min(mydict.values()))
print(max(mydict.values()))
print(mydict)
print(type(mydict.keys()))
print(type(mydict.values()))
print(random.choices(list(mydict.keys()), weights = list(mydict.values()), k = 14))
if 'a' in mydict.keys():
    mydict["b"]+=1
print(mydict)