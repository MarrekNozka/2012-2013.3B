#!/usr/bin/python
# -*- coding: utf8 -*-

import mujModul

print mujModul.cislo
mujModul.inc()
print mujModul.cislo

mujModul.cislo = 20
print mujModul.cislo
mujModul.inc()
print mujModul.cislo

print mujModul.soucet(2,7)

####################################################


import mujModul as moje
print moje.cislo
print dir(moje)
print moje.__name__
print moje.__file__
print moje.__doc__

####################################################

from mujModul import cislo # prom. cislo je KOPIE prom. mujModul.cislo
from mujModul import soucet

print cislo
print mujModul.cislo
mujModul.cislo=894
print cislo

print soucet(22,76)

from mujModul import * 


####################################################
import sys

sys.path.insert(0,'./mm/')
sys.path = ['./mm'] + sys.path
#print sys.path
import mod
