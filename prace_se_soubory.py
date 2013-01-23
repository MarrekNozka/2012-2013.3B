#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  prace_se_soubory.py
# Datum:   23.01.2013 08:15
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha:   úvod do práce se soubory
############################################################################

# f je tzv. ovladdač -- handler
f = open("soubor.txt", "r")

# čtu řádek
radek = f.readline()
print "----------------"
print radek,
print "----------------"

# čtu jeden znak -- jeden Byte
znak = f.read(1)
print znak
znak = f.read(1)
print znak
znak = f.read(1)
print znak


# přečtu celý soubor
while True:
    radek = f.readline()
    if radek == '' :  # na konci souboru vrátí fce readline() prázdný řetězec
        break
    print radek,

# uzavření soubru
f.close()
############################################################################

f = open('novy.txt', 'w')
f.write("Toto je jeden řádek")
f.write("toto nenní další řádek protože jsem ho neukončil")
f.write("ukončím ho a až teď\n")
f.write("nový řádek")

f.close()
############################################################################

f = open('soubor.txt', 'a')
import time

f.write( str( time.time() )+'\n' )

f.close()
############################################################################

import sys

# čtení z klávesnice
radek = sys.stdin.readline()
# tisknu na obrazovku
sys.stdout.write("toto se m tisknu\n")
sys.stdout.write(radek)

