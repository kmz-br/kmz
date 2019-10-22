#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "Rodrigo da Costa"
__copyright__ = "Copyright (C) 2019, kmz human password generator"
__version__ = "2.0.0 beta"
__email__ = "suporte@4rcm.com"
"""
crunch - wordlist generator
https://sourceforge.net/projects/crunch-wordlist/files/
https://gitlab.com/kalilinux/packages/crunch
"""
import os
import subprocess

import kmz
import temp

kmz.delete()
kmz.welcome()
kmz.linha(80)
mn1 = mn0 = sair = ''
kmz.mn0()
while mn0 != '0' and '1' and '2' and '3':
    kmz.linha(80)
    mn0 = str(input('opção: 0, 1, 2, 3, 4 : ')).strip()
    if mn0 == '0':
        break
    elif mn0 == '1':
        break
    elif mn0 == '2':
        break
    elif mn0 == '3':
        kmz.about(1)
    elif mn0 == '4':
        break
kmz.linha(80)
words = str(input('lista de palavras: ')).lower().strip().split()
kmz.linha(80)
bd = {'soft': 'crunch',
      'ext': '.txt',
      'num': '0123456789',
      'alf': 'abcdefghijklmnopqrstuvwxyz',
      'alfu': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
      'per': 'personalizado'
      }
kmz.mn1(pa=bd)
while mn1 != '0' and '1' and '2' and '3':
    mn1 = str(input('opção: 0, 1, 2, 3 = ')).strip()
    if mn1 == '0':
        crt = f'{bd["num"]}'
        while True:
            p0 = str(input('máximo de repetição: '))
            if p0.isnumeric() and int(p0) > 0:
                b4 = f'-d {int(p0)}%'
                break
            elif p0.lower() == 'n':
                b4 = ''
                break
    elif mn1 == '1':
        crt = bd["alf"]
        break
    elif mn1 == '2':
        crt = bd["alfu"]
        break
    elif mn1 == '3':
        crt = str(input('caracteres personalizado: ')).strip()
        break
kmz.linha(80)
print('tamanho mínimo e máximo da senha')
while True:
    p1 = str(input('mínimo: '))
    if p1.isnumeric() and int(p1) > 0:
        psw1 = int(p1)
        break
while True:
    p2 = str(input('máximo: '))
    if p2.isnumeric() and int(p2) > 0:
        psw_mx1 = int(p2)
        break
kmz.linha(80)
print('por favor aguarde... O crunch iniciou a criação dos dicionários:')
kmz.linha(80)
database = []
for dg in range(0, 2):  # Diagnostico
    temp.diag(arg=words)
for a in range(0, len(words)):  # setor a
    database.append(words[a].lower())
    database.append(words[a].upper())
    if 'i' in words[a]:
        database.append(kmz.replacei(words[a], 1))
        database.append(kmz.replacei(words[a], 2))
    if 'l' in words[a] and words[a][len(words[a])-1] != 'l':
        if words[a][words[a].index("l") + 1].lower() != 'l':
            database.append(kmz.replacel(words[a], 1))
            database.append(kmz.replacel(words[a], 2))
    database.append(kmz.upper_lower(words[a], 1))
    database.append(kmz.upper_lower(words[a], 2))
    database.append(kmz.upper1(words[a], 1))
    database.append(kmz.upper1(words[a], 2))
    database.append(kmz.upper1(words[a], 3))
    database.append(kmz.inverse(words[a], 0))
    database.append(kmz.inverse(words[a], 1))
    database.append(kmz.inverse(words[a], 2))
    database.append(kmz.inverse(words[a], 3))
    database.append(kmz.inverse(words[a], 4))
ct1 = 1
blc = []
for b in range(0, len(database)):  #setor b
    psw_mx = psw_mx1
    psw = psw1
    if psw - len(database[b]) <= 7:
        ct3 = len(database[b])
        ct2 = 1
        if os.name == 'nt':
            while psw <= psw_mx:
                if psw > len(database[b]):
                    b1 = f'{bd["soft"]} {psw} {psw} {crt} -t'
                    b2 = f'{"@" * (psw - len(database[b]))}'
                    b3 = f'{os.path.dirname(os.path.realpath(__file__))}/temp/'
                    blc.append(f"{b1} {b2}{database[b]} {b4} -o {b3}{ct2}{ct1}a{bd['ext']} &")
                    blc.append(f"{b1} {database[b]}{b2} {b4} -o {b3}{ct2}{ct1}b{bd['ext']} &")
                psw += 1
        elif os.name == 'posix':
            while psw <= psw_mx:
                if psw > len(database[b]):
                    b1 = f'{bd["soft"]} {psw} {psw} {crt} -t'
                    b2 = f'{"@" * (psw - len(database[b]))}'
                    b3 = os.path.dirname(os.path.realpath(__file__))
                    subprocess.call(f"{b1} {b2}{database[b]} {b4} -o {b3}/temp/{ct2}{ct1}a{bd['ext']}", shell=True)
                    subprocess.call(f"{b1} {database[b]}{b2} {b4} -o {b3}/temp/{ct2}{ct1}b{bd['ext']}", shell=True)
                    ct2 += 1
                    ct3 += 1
                psw += 1
    ct1 += 1
if os.name == 'nt':
    sbs = f"c{blc[0]} " + ' '.join(blc[1:])
    os.chdir('kmz')
    subprocess.call(f"cmd /{sbs}", shell=True)
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    temp.merge()
elif os.name == 'posix':
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    temp.merge()


