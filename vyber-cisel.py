#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  vyber-cisel.py
# Datum:   21.11.2012 08:23
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha:   program bere čísla ze vstup na výstup vypisuje nejprve 
#          záporná čísla až potom kladná
############################################################################

radek = raw_input("zadej mi sem čísla >> ")
cisla = radek.split()

kladna = []   # vytvořím prázdný seznam, do kterého budu přídávat čísla
zaporna = []
i = 0
while i<len(cisla):
    cislo = float(cisla[i]) # převedu řetězec na číslo
    if cislo > 0:
        kladna = kladna + [ cislo ] # přídám do seznamu pomocí operátoru +
    else:
        zaporna.append(cislo)   # přídám do seznamu pomocí append    
    i += 1

# vypíšu kladná 
i = 0
while i<len(kladna):
    print kladna[i]
    i +=1 
# vypíšu záporná čísla v opačném pořadí
i = len(zaporna)-1
while i>=0:
    print zaporna[i]
    i = i - 1 

############################################################################
# a teď se naučíme cyklus for
print "ukázka cyklu FOR"

for i in (1,2,3):
    print i

print "####################"

for i in kladna:
    print i
zaporna.reverse()
for i in zaporna:
    print i

print "####################"
# http://docs.python.org/2.7/library/functions.html?highlight=range#range
for i in range(5,20,3):
    print i,
