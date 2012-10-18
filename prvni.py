# -*- coding: utf8 -*-

# poznámka se píše za dvojkříž (hash)

"poznámku lze zapsat i jako řetězec"

""" pokud začnu řetěze 3x uvozovka je to výce

řádkový


řetězec"""

print "Hello World"


# příkaz input načte číslo
cislo = input("Zadej číslo: ".decode("utf-8"))

if cislo<0:
    print u"cislo je zaporne"
    print cislo
else:
    print "číslo ti neukážu"
    print "protože je kladné"
    
print "tento řádek se tiskne vždycky"

if not(cislo>0 and cislo<10) :
    rint "internval (-oo;> U <10;+oo) "