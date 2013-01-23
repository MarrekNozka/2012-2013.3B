#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  fce_global_local.py
# Datum:   16.01.2013 08:41
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha:   Globální a lokolní proměnné
############################################################################

def funkceA():
    # globální prom. je možné číst
    print "A:",a,b, id(a), id(b)

def funkceB():
    a=30  # a je lokální proměná dostupná jen z této funkce
    print "B:",a,b , id(a), id(b)

def funkceC():
    # x je lokální proměná dostupná jen z této funkce
    x=123456
    print "C:",x

def funkceD():
# y je globální proměná přístupná z této funkce i z hlavního programu
    global y
    y=123456
    print "D:",y
############################################################################

# Hlavní program
    
a=10  # Globání proměnné
b=77

y=9999999

print a,b, id(a), id(b)
funkceA()
print a,b
funkceB()
print a,b
funkceC()
#print x # CHYBA, x je definová uvnitř funkce a proto není vidět
funkceD()
print y

