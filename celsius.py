#!/usr/bin/env python
# -*- coding: utf8 -*-
# Datum:   Wed Oct 24 08:51:05 2012
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha: 
# Popis:   převodní tabulka °C -> °F

C = 0
while C<=30:
    F= 9.0*C/5 + 32
#    print C,"°C = ",F,"°F"
    print u"{0:4d}°C = {1:7.3f}°F".format(C,F)
    C= C+1
print 9.0/4

