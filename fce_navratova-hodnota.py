#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  fce_navratova-hodnota.py
# Datum:   16.01.2013 09:07
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha:   funkce a její návratová hodnota
############################################################################
#  Definice funkcí

def secti(a,b):
    soucet = a + b
    return soucet # ukončí funkci a vydá hodnotu
    bla= 12   # tyto řádky už se nevykonají, protože jsou za return
    print bla

def mocnina(x,n):
    return x**n

def faktorian(n):
    vysl = 1
    i=1
    while i<=n:
        vysl = vysl * i
        i = i +1
    return vysl

############################################################################
#   Hlavní program

x=10
y=13

suma = secti(x,y)
print suma
print secti(22,49)

print mocnina(2,16)

print "5! =", faktorian(5)
print "10! =", faktorian(10)
