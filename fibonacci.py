#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  fibonacci.py
# Datum:   05.12.2012 08:22
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha:   Fibonacciho posloupnost
############################################################################

# podprogram
def Fib(n):
    if n < 0:
        print "Index musí být kladný"
    elif n == 0:
        print 0
    elif n == 1:
        print 0,1
    else:
        print 0,1,
        # v proměný si uchovávám hodnoty předhozích dvou čísel
        (F_2, F_1 ) = (0,1) 
        # řídící proměná cyklu
        i = 2 
        while i<=n :
            i += 1
            Fn = F_2 + F_1
            print Fn,
            (F_2, F_1) = ( F_1, Fn)

# rekurzivní definice
def FibR(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n>1:
        return FibR(n-1)+FibR(n-2)


maximum = input('zadej maximální index Fibonacciho poslounosti > ')
Fib(maximum)
print '\n######################\n'
print FibR(maximum)


