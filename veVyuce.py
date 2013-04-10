# -*- coding: utf8 -*-
# Soubor:  veVyuce.py
# Datum:   10.04.2013 08:58
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha:   Modul s funkcemi, které tvoříme ve výuce
############################################################################


def myMax(seznam):
    myMax = seznam[0]
    for i in seznam[1:]:
        if i>myMax :
            myMax = i
    return myMax
