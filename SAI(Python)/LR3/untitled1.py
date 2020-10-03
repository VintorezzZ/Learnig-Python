# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 22:32:53 2020

@author: VintorezzZ
"""

import math

def PloshadOfTriangle():
    a = float(input('Input a: '))
    b = float(input('Input b: '))
    c = float(input('Input c: '))
    p = (a + b + c) / 2
    s = float('%.6f' % math.sqrt(p*(p - a)*(p - b)*(p - c)))
    print('Perimetr = ',p)
    print('\nПлощадь треугольника равна:',s)