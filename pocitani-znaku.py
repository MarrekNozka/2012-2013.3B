#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  pocitani-znaku.py
# Datum:   17.04.2013 09:05
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha:   počítadlo znaků
############################################################################

import sys
from sys import stdin, stdout, stderr
############################################################################

cesta= sys.argv[0]

# otevřeme souboru
f = open(cesta, 'r')

pocty = {} # počty znaků
# procházím soubor znak po znaku:
while True:
    znak = f.read(1) # na konci souboru .read() vrátí prázndný  řetězec
    if znak == '': 
        break
    if znak == ' ' or znak == '\n' or znak == '\t':  
        continue   # přeskočím bílé znaky
    if pocty.has_key(znak) :
        pocty[znak] +=  1 
    else :
        pocty[znak] = 1

# uzavřu soubor
f.close()

# Tisk výsledků
for klic in pocty.keys() :
    print klic, '->', pocty[klic]

