#Copyright (C) 2019 Rodrigo Costa - suporte@4rcm.com
#kmz human password generator beta 1.2 and crunch - wordlist generator (https://sourceforge.net/projects/crunch-wordlist/files/)

crt = mn0 = ''
bd = {'soft': 'crunch',
      'ext': '.txt &',
      'num': '0123456789',
      'alf': 'abcdefghijklmnopqrstuvwxyz',
      'alfu': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
      'per': 'Personalizado'
      }
nome = str(input('Lista de palavras: ')).lower().strip().split()
print(f'CARACTERES\n [0] - {bd["num"]}\n [1] - {bd["alf"]}\n [2] - {bd["alfu"]}\n [3] - {bd["per"]}')
while mn0 != '0' and '1' and '2' and '3':
    mn0 = str(input('Opção: 0, 1, 2, 3 = ')).strip()
    if mn0 == '0':
        crt = f'{bd["num"]}'
        break
    elif mn0 == '1':
        crt = bd["alf"]
        break
    elif mn0 == '2':
        crt = bd["alfu"]
        break
    elif mn0 == '3':
        per = str(input('Caracteres personalizado: ')).strip()
        crt = per
        break
print('Máximo de repetição (Ex: 000, aaa) recomendado 2\nDigite N para não informar repetição')
pswre = str(input('Máximo de repetição: ')).strip().lower()
psw_spc = str(input('Ativar senhas especiais: S/N: ')).strip().lower()
psw_cel = str(input('Ativar senha com número de celular: S/N '))
print('='*70)
sm = 1
psw = 8
cbr = 0

while psw <= 11:
    for c in range(0, len(nome)):
        a00 = f'{bd["soft"]} {psw + 1} {psw + 1} {crt} -t'
        a1 = f'{bd["soft"]} {psw} {psw} {crt} -t'
        a12 = len(nome[c])
        a14 = f'{bd["soft"]} {a12 + 9} {a12 + 9} 0123456789 -t'
        a15 = f'{"@"*6} -o '
        if 'n' in pswre:
            a11 = ''
        else:
            if mn0 == '0':
                a11 = f' -d {pswre}%'
            else:
                a11 = f' -d {pswre}@'
        a13 = f'{psw}{bd["ext"]}'
        #INICIO do módulo de upper e lower -> ExEmPlo e eXeMpLo
        lst2 = []
        lst3 = []
        for f in range(0, len(nome[c])):
            if f % 2 == 0:
                lst2.append(nome[c][f].upper())
            else:
                lst2.append(nome[c][f].lower())
            if f % 2 != 0:
                lst3.append(nome[c][f].upper())
            else:
                lst3.append(nome[c][f].lower())
            a17 = ''.join(lst2)
            a18 = ''.join(lst3)
        # FIM do módulo de upper e lower
        if (psw - len(nome[c])) <= 7:
            if psw > len(nome[c]):
                print(f'{a1} {nome[c]}{"@" * (psw-len(nome[c]))}{a11} -o {sm}b{a13}')
                print(f'{a1} {"@" * (psw - len(nome[c]))}{nome[c]}{a11} -o {sm}c{a13}')
                print(f'{a1} {nome[c].capitalize()}{"@" * (psw - len(nome[c]))}{a11} -o {sm}d{a13}')
                print(f'{a1} {"@" * (psw - len(nome[c]))}{nome[c].capitalize()}{a11} -o {sm}e{a13}')
                print(f'{a1} {nome[c].upper()}{"@" * (psw - len(nome[c]))}{a11} -o {sm}f{a13}')
                print(f'{a1} {"@" * (psw - len(nome[c]))}{nome[c].upper()}{a11} -o {sm}g{a13}')
                print(f'{a1} {nome[c][::-1]}{"@" * (psw - len(nome[c]))}{a11} -o {sm}h{a13}')
                print(f'{a1} {"@" * (psw - len(nome[c]))}{nome[c][::-1]}{a11} -o {sm}i{a13}')
                print(f'{a1} {nome[c][::-1].capitalize()}{"@" * (psw - len(nome[c]))}{a11} -o {sm}j{a13}')
                print(f'{a1} {"@" * (psw - len(nome[c]))}{nome[c][::-1].capitalize()}{a11} -o {sm}k{a13}')
                print(f'{a1} {nome[c][::-1].upper()}{"@" * (psw - len(nome[c]))}{a11} -o {sm}l{a13}')
                print(f'{a1} {"@" * (psw - len(nome[c]))}{nome[c][::-1].upper()}{a11} -o {sm}m{a13}')
                print(f'{a1} {"@" * (psw - len(nome[c]))}{a17}{a11} -o {sm}n{a13}')
                print(f'{a1} {"@" * (psw - len(nome[c]))}{a18}{a11} -o {sm}0{a13}')
            if psw_spc[0] == 's':
                a2 = psw - len(nome[c])
                if 'a' in nome[c] and len(nome[c]) >= 8 and cbr == 0:
                    print(f'{bd["soft"]} {psw - a2} {psw - a2} @ -t {nome[c].replace("a", "@")} -o {sm}ps{a13}')
                    cbr += 1
                if 'l' in nome[c]:
                    print(f'{a00} {nome[c].replace("l", "ll")}{"@" * (psw - len(nome[c]))}{a11} -o {sm}al{a13}')
                    print(f'{a00} {"@" * (psw - len(nome[c]))}{nome[c].replace("l", "ll")}{a11} -o {sm}bl{a13}')
                    print(f'{a00} {nome[c].replace("l", "ll").capitalize()}{"@" * (psw - len(nome[c]))}{a11} -o {sm}cl{a13}')
                    print(f'{a00} {"@" * (psw - len(nome[c]))}{nome[c].replace("l", "ll").capitalize()}{a11} -o {sm}dl{a13}')
                    print(f'{a00} {nome[c].replace("l", "ll").upper()}{"@" * (psw - len(nome[c]))}{a11} -o {sm}el{a13}')
                    print(f'{a00} {"@" * (psw - len(nome[c]))}{nome[c].replace("l", "ll").upper()}{a11} -o {sm}fl{a13}')
                if 'i' in nome[c] and len(nome[c]) >= 5:
                    a = nome[c].index('i')
                    b = f'{nome[c][:a]}y{nome[c][a + 1:]}'
                    print(f'{a1} {b}{"@" * (psw - len(nome[c]))}{a11} -o {sm}ai{a13}')
                    print(f'{a1} {"@" * (psw - len(nome[c]))}{b}{a11} -o {sm}bi{a13}')
                    print(f'{a1} {b.capitalize()}{"@" * (psw - len(nome[c]))}{a11} -o {sm}ci{a13}')
                    print(f'{a1} {"@" * (psw - len(nome[c]))}{b.capitalize()}{a11} -o {sm}di{a13}')
                    print(f'{a1} {b.upper()}{"@" * (psw - len(nome[c]))}{a11} -o {sm}ei{a13}')
                    print(f'{a1} {"@" * (psw - len(nome[c]))}{b.upper()}{a11} -o {sm}fi{a13}')
            opr = [88, 81, 99]
            for e in range(0, len(opr)):
                if psw_cel[0] == 's':
                    print(f'{a14} {nome[c]}9{opr[e]}{a15}{sm}{opr[e]}cel1{a13}')
                    print(f'{a14} {nome[c].upper()}9{opr[e]}{a15}{sm}{opr[e]}cel2{a13}')
                    print(f'{a14} {nome[c].capitalize()}9{opr[e]}{a15}{sm}{opr[e]}cel3{a13}')
                    print(f'{a14} {nome[c][::-1]}9{opr[e]}{a15}{sm}{opr[e]}cel4{a13}')
                    print(f'{a14} {nome[c][::-1].capitalize()}9{opr[e]}{a15}{sm}{opr[e]}cel5{a13}')
                    print(f'{a14} {nome[c][::-1].upper()}9{opr[e]}{a15}{sm}{opr[e]}cel6{a13}')
                    opr1 = a12 - 2
                    opr2 = f'{nome[c][opr1:].upper()}'
                    print(f'{a14} {nome[c][:opr1]}{opr2}9{opr[e]}{a15}{sm}{opr[e]}cel7{a13}')
                    print(f'{a14} {nome[c][:opr1].capitalize()}{opr2}9{opr[e]}{a15}{sm}{opr[e]}cel8{a13}')
    sm += 1
    psw += 1
print('python kmz_merge.py &')
