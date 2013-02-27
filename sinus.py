#!/usr/bin/env python
# -*- coding: utf8 -*-
# Soubor:  sinus.py
# Datum:   27.02.2013 08:30
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Popis:   sinusovky
###################################################3 
import matplotlib as mpl
mpl.use('GTKAgg')
mpl.use('Qt4Agg')
#mpl.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#mpl.rc('font',**{'family':'serif','serif':['Palatino']})
#mpl.rc('lines', linewidth=2, color='r')
mpl.rc('font', family = 'serif', serif = 'cmr10') 
mpl.rcParams['text.usetex']=True
mpl.rcParams['text.latex.unicode']=True

import numpy as num
import scipy as sci
import pylab as lab
from pylab import pi
#interactive mode 
#lab.ion()
#lab.ioff()

f=50

t = lab.linspace(0,0.035,100)
u = 2 * lab.sin(2*pi*f*t)

lab.plot(t,u)
lab.grid(which='both')
lab.xlim( [min(t),max(t)] )
lab.ylim( [-4,4] )

#lab.xticks(lab.arange(0,0.035,0.002), 1000* lab.arange(0,0.035,0.002))
#lab.yticks( lab.arange(-4,4,0.5) )

lab.xlabel('t[s]')

lab.ylabel('u[V]')
lab.title(ur'$u=\sin(2 \pi f t)$')


i = 2 * lab.sin(2*pi*f*t+ lab.deg2rad(0) )
lab.plot(t,i)

lab.plot(t,u*i)


lab.show()

