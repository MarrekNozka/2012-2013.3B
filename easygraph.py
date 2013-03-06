#!/usr/bin/env python
# -*- coding: utf8 -*-
# Soubor:  easygraph.py
# Datum:   06.03.2013 08:41
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha:   Tvorba grafu ze vstupního souboru
###################################################3 

import sys
import pylab as lab
from pylab import pi


if len(sys.argv) > 1:
    soubor = sys.argv[1]
else:
    soubor=raw_input("Zadej jméno souboru > ")
 
# otevřeme soubor
f = open(soubor,'r')

x = f.readline().strip().split()
y = f.readline().strip().split()



# uzavřu soubor
f.close()

lab.plot(x,y)
lab.show()
