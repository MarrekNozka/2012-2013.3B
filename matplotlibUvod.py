#!/usr/bin/env python
# -*- coding: utf8 -*-
# Soubor:  matplotlibUvod.py
# Datum:   13.02.2013 08:41
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha:   úvod do matplotlib
###################################################3 

import pylab as lab
from pylab import pi

x = ( 0,1,3,6,7 )
y=  lab.array(( 5,4,6,4,2 ))

#http://matplotlib.org/api/pyplot_api.html?highlight=pyplot.plot#matplotlib.pyplot.plot
fig1=lab.figure(1)
lab.plot(x,y,'r:+')
lab.plot(x,y+1,'#aa0000', linestyle='-.', alpha=0.5, 
          marker='o', markerfacecolor='green', markersize=20)
lab.grid()
lab.title('Titulek')
lab.xlabel(u'osa x')
lab.ylabel(u'závislá proměnná')
lab.xlim([-2,10])
lab.ylim([-1,8])

# hladká řívka
newX = lab.linspace(min(x), max(x),300)
from scipy.interpolate import spline
newY = spline(x,y,newX)
lab.plot(newX,newY,'b-')

fig2=lab.figure(2)
# čas od 0 do 3, 100 hodnot
t=lab.linspace(0,0.8,100)
# napětí
f=3
u= 2+ lab.sin(2*pi*f*t+pi/3.)
lab.plot(t,u,'b-')
lab.title('Sinus')
lab.xlabel(u't [s]')
lab.ylabel(u'sin(2pift)')
lab.grid()
lab.xlim([0,0.8])
lab.ylim([0,4])


#### VACH
fig3=lab.figure(3)
u= (0, 0.3, 0.5, 0.8, 1,  2,  3)
i= (0, 0.1, 0.5, 1  , 3, 10, 30)

lab.plot(u,i,'ro',label='vzorky')
lab.grid()
lab.xlim( (-1, 4) )
lab.ylim( [-1, 35] )
# lomená čára
lab.plot(u,i,'y-',label='takto to nechci')
#hladká křivka
import scipy.interpolate as interpol
# vyrobím znovu osu x ale s mnohem větším počtem (300) bodů
newU=lab.linspace( min(u), max(u), 300  )
# vyrobím interpolační funkci
funkce=interpol.UnivariateSpline(u,i)
# právě vyrobená funkce mi vypočítá nové hodnoty osy Y
newI = funkce(newU)
lab.plot(newU,newI,'b-', label=u'proložím hladkou křivkou')

# ještě jednou, ale hladká křivka bude procházet všemi body
funkce=interpol.UnivariateSpline(u,i,s=0)
newI = funkce(newU)
lab.plot(newU,newI,'g-', label=u'křivka prochází všemi body')


lab.legend(loc='best')

lab.close(fig1)
lab.close(fig2)
fig3.show()
lab.show()

