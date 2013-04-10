#!/usr/bin/python
# -*- coding: utf8 -*-

import veVyuce
import random

s = [ random.randint(-100,100) for _ in range(10) ]

print s

print veVyuce.myMax(s)
