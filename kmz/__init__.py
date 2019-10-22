def welcome():
    print(f'''                                 _   _   _  
                                / \ / \ / \ 
                               ( k | m | z )
                                \_/ \_/ \_/ \n                     human password generator 2.0.0 beta''')


def linha(ta):
    return print(f"{'-' * ta}")


def about(arg=0):
    import platform
    if arg == 1:
        print(
            f'Sistema Operacional: {platform.system()} {platform.release()} {platform.architecture()[0]} {platform.version()}')
        print(platform.processor())
        print(platform.machine())
    elif arg == 2:
        print(
            f'Sistema Operacional: {platform.system()} {platform.release()} {platform.architecture()[0]} {platform.version()}')


def delete():
    import os
    for m in os.listdir():
        if '.txt' in m:
            os.remove(m)
    for k in os.listdir('temp'):
        if '.txt' in k:
            os.remove(f'temp/{k}')


def replacei(valor, pa):  # subtituindo o primeiro i do nome por um y
    if pa == 1:
        return f'{valor[:(valor.index("i"))]}y{valor[(valor.index("i")) + 1:]}'
    elif pa == 2:
        return f'{valor[:(valor.index("i"))]}y{valor[(valor.index("i")) + 1:]}'.upper()


def replacel(valor, pa):  # subtituindo o primeiro l do nome por ll
    if pa == 1:
        return f'{valor[:(valor.index("l"))]}ll{valor[(valor.index("l")) + 1:]}'
    elif pa == 2:
        return f'{valor[:(valor.index("l"))]}ll{valor[(valor.index("l")) + 1:]}'.upper()


def upper_lower(valor, pa):  # alterna as letras entre maiuscula e minusculas
    lst2 = []
    lst3 = []
    for f in range(0, len(valor)):
        if f % 2 == 0:
            lst2.append(valor[f].upper())
            lst3.append(valor[f].lower())
        else:
            lst2.append(valor[f].lower())
            lst3.append(valor[f].upper())
    if pa == 1:
        return ''.join(lst2)
    if pa == 2:
        return ''.join(lst3)
    lst2.clear()
    lst3.clear()


def upper1(valor, pa):  # primeira letra em maiuscula ou primeira e segunda em maiuscula
    lst4 = []
    if pa == 1:
        return valor.capitalize()
    elif pa == 2:
        for g in range(0, len(valor)):
            if g < 2:
                lst4.append(valor[g].upper())
            else:
                lst4.append(valor[g].lower())
        return ''.join(lst4)
    elif pa == 3:
        for h in range(0, len(valor)):
            if h < 3:
                lst4.append(valor[h].upper())
            else:
                lst4.append(valor[h].lower())
        return ''.join(lst4)
    lst4.clear()


def inverse(valor, pa=0):  # inverte o nome
    lst5 = []
    if pa == 1:
        return valor[len(valor)::-1].capitalize()
    elif pa == 2:
        for i in range(0, len(valor)):
            if i < 2:
                lst5.append(valor[len(valor)::-1][i].upper())
            else:
                lst5.append(valor[len(valor)::-1][i].lower())
        return ''.join(lst5)
    elif pa == 3:
        for i in range(0, len(valor)):
            if i < 3:
                lst5.append(valor[len(valor)::-1][i].upper())
            else:
                lst5.append(valor[len(valor)::-1][i].lower())
        return ''.join(lst5)
    elif pa == 4:
        return valor[len(valor)::-1].upper()
    elif pa == 0:
        return valor[len(valor)::-1]


# MENUS
def mn0():
    print(
        f'[0]- lista básica  [1]- lista full  [2]- lista/celular  [3]- sobre  [4]- sair')


def mn1(pa):
    print(f'CARACTERES\n [0] - {pa["num"]}\n [1] - {pa["alf"]}\n [2] - {pa["alfu"]}\n [3] - {pa["per"]}')
