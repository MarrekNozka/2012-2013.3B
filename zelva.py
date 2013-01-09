#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  zelva.py
# Datum:   09.01.2013 08:45
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha:   funkce
############################################################################


import turtle as t

# nastavení
t.speed(1)
t.shape("turtle")

# kreslí n-úhlelník
def tvar(kroky=100,n=6):
    for _ in range(n):
        t.forward(kroky)
        t.left(360./n)


tvar()     # 6-úhelník, 100 kroků
tvar(200)  # 6-úhelník, 200 kroků
tvar(150,3)  # 3-úhelník, 150 kroků

tvar(n=13) # 13-úhelník, 100 kroků

tvar(n=8,kroky=90)

t.exitonclick()
