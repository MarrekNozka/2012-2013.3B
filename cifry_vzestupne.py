#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  cifry_vzestupne.py
# Datum:   14.11.2012 08:17
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha: Je dána posloupnost celých čísel. Vypište jen ta čísla,
#        jejíchž cifry jsou ve vzestupném pořadí.  
############################################################################

radek = raw_input("zadej mezerou oddělená čísla: ")
cisla = radek.split()

# podprogram rozhodne jestli cilo c obsahuje cifry ve vzestupnem poradi
def jeCisloOK(c):
    if len(c)<=1:  # jednociferná čísla nemají cifry ve vzestupném pořadí
        return False 
    i = 1
    while i<len(c):
        if not( int(c[i-1]) < int(c[i]) ):
            return False    # ukončí podprogram
        i += 1  # posunu i pro další obrátku
    return True  # pokud projdu všechno a nezjistím problém vrátím True



i = 0    # i je řídící proměná
while i < len(cisla):
    cislo = cisla[i]
    if jeCisloOK(cislo) :
        print cislo
    i += 1  # posunu si i pro daší obrátku cyklu

print "#### ještě jesnou bez podprogramu ######"

i = 0    # i je řídící proměná
while i < len(cisla):
    cislo = cisla[i]
    if len(cislo)<=1:
        continue # skočí na další obrátku cylku a znovu kontroluje podmínku
    j = 1   # řídící proměná cyklu 
    OK = True  # pamatuji si jestli mám číslo tisknout
    while j<len(cislo):
        if not( int(cislo[j-1]) < int(cislo[j]) ):
            OK = False
            break # okamžitě vyskočí z cyklu
        j += 1  # posunu j pro další obrátku
    if OK:
        print cislo
    i += 1  # posunu si i pro daší obrátku cyklu

