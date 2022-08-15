#https://github.com/StatguyUser/BaselineRemoval/commit/6310a0bb142b26808db43943d4c445498a117313
from BaselineRemoval import BaselineRemoval
from RamanFilter import RamanFilter
import numpy as np
import sys
from matplotlib import pyplot as plt


#input_array = [10, 20, 1.5, 5, 2, 9, 99, 25, 47]
filepath = 'd:/Logan Moore Peak Analysis/'
filename = 'TA-Male-4-2.csv'
ta = RamanFilter(filepath, filename, 'TA Muscle')

polynomial_degree = 2    # only needed for Modpoly and IModPoly algorithm

baseObj = BaselineRemoval(ta.y)
ta.mPoly = baseObj.ModPoly(polynomial_degree)
ta.iPoly = baseObj.IModPoly(polynomial_degree)
ta.zhangFit = baseObj.ZhangFit()

#print('Original input:', ta.y)
#print('Modpoly base corrected values:', ta.mPoly)
#print('IModPoly base corrected values:', ta.iPoly)
#print('ZhangFit base corrected values:', ta.zhangFit)

ta.plot_original()
ta.plot_filtered()
ta.plot_zhang_fit()
ta.zoom_zhang_fit(900, 1800)





