# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 06:31:41 2022

@author: eriss
"""
import matplotlib.pyplot as plt

x = [x for x in range(101)]
y = [y**2 for y in x]

plt.plot(x,y, '-*')
plt.show()
