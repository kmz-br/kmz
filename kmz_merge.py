#Copyright (C) 2019 Rodrigo Costa - suporte@4rcm.com
#mesclar arquivos de texto
#kmz merge 1.5_beta

from os import listdir, remove, path
import sys

host = path.dirname(path.realpath(__file__))
sys.stdout = open(f'{host}/dictionary.txt', 'w')

dir = []
for c in listdir(f'{host}/'):
    if '.txt' in c and not "dictionary"in c:
       dir.append(c)
with open("dictionary.txt", "w") as file:
    for temp in dir:
        with open(temp, "r") as t:
            file.writelines(t)
for e in dir:
       remove(e)
