#!/usr/bin/env python
# -*- coding: utf8 -*-
# Datum:   Wed Oct 24 08:51:05 2012
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha: 
# Popis:   převodní tabulka °C -> °F

""" String format:
http://docs.python.org/2.7/library/stdtypes.html?highlight=str.format#string-formatting
"""
while True:
    start = input('start = ')
    konec = input('konec = ')
    krok = input(' krok = ')

    C = start
    while C<=konec:
        F= 9.0*C/5 + 32
#       print C,"°C = ",F,"°F"
        print u"{0:.2f}°C = {1:7.2f}°F".format(C,F)
        C = C + krok

