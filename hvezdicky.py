#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  hvezdicky.py
# Datum:   28.11.2012 08:39
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha:   trojúhelník z hvezdicek
############################################################################

import random
############################################################################
r = input("kolik řádků? >>")


pMezer=r-1
pZnaku=1

znaky=("#", '@', '§', '%', 'A')

for _ in range(r):
    tisk=''
    for _ in range(pZnaku):
        nahoda=random.randint(0,len(znaky)-1)  # náhodné číslo v rozshahu indexů 'znaky'
        tisk = tisk + znaky[ nahoda ]
    print pMezer*' ' + tisk
    pZnaku +=2
    pMezer -=1
