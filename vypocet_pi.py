#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  vypocet_pi.py
# Datum:   07.11.2012 09:11
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha:   Výpočet čísla pi 
#         http://cs.wikipedia.org/wiki/Pí_(číslo)#Odhad_.CF.80


pi = 0
jmenovatel =1 
citatel = 4.0
znamenko = 1

while jmenovatel<1e9 :
    pi = pi + znamenko*citatel/jmenovatel
    jmenovatel = jmenovatel + 2
    znamenko = znamenko * (-1)
print pi

import math
print math.pi

