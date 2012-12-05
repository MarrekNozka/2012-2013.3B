#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  fibonacci.py
# Datum:   05.12.2012 08:22
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha:   Fibonacciho posloupnost
############################################################################


maximum = input('zadej maximální index Fibonacciho poslounosti > ')


if maximum < 0:
    print "Index musí být kladný"
elif maximum == 0:
    print 0
elif maximum == 1:
    print 0,1
else:
    print 0,1,
    F_2 = 0  # v proměný si uchovávám hodnoty předhozích dvou čísel
    F_1 = 1
    i = 2    # řídící proměná cyklu
    while i<=maximum :
        i = i + 1
        Fn = F_2 + F_1
        print Fn,
        F_2 = F_1
        F_1 = Fn
