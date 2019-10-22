def diag(arg):
    from os import listdir, path, chdir
    import platform
    import sys
    sys.stdout = open('diagnostico.txt', 'w')
    print(f'Sistema Operacional: {platform.system()} {platform.release()} {platform.architecture()[0]} {platform.version()}')
    print(f'Processador: {platform.processor()}')
    print(f'Plataforma: {platform.machine()}')
    print(f'Python Versão: {platform.python_build()}')
    print(f'Python compilador: {platform.python_compiler()}')
    print(f'Lista usada: {arg}')
    print(f'Arquivos do diretório principal: {listdir()}')
    print(f'Arquivos do diretório /temp: {listdir(path.dirname(path.realpath(__file__)))}')


def merge():
    from os import listdir, remove
    import sys

    sys.stdout = open('dictionary.txt', 'w')
    diret = []
    for mc in listdir('temp/'):
        if '.txt' in mc and not "dictionary" in mc:
            diret.append(f'temp/{mc}')
    with open("dictionary.txt", "w") as file:
        for arq in diret:
            with open(arq, "r") as t:
                file.writelines(t)
    for mb in diret:
        remove(mb)
