# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 14:42:35 2020

@author: rowe1
"""

import time
import matplotlib.pyplot as plt
import random

i = [10**j for j in range(3, 7)]

list_set = []
sort_set = []
timsort = []
for j in i:
    a = list(range(1, j))
    random.shuffle(a)
    
    # list set sort
    t0 = time.time_ns()
    sorted(list(set(a)))
    list_set.append(time.time_ns() - t0)
    
    # set sort
    t0 = time.time_ns()
    sorted(set(a))
    sort_set.append(time.time_ns() - t0)
    
    # timsort
    t0 = time.time_ns()
    sorted(a)
    timsort.append(time.time_ns() - t0)

plt.close('all')
plt.figure()
plt.loglog(i, list_set, 'r-', lw = 2, label = 'list_set')
plt.loglog(i, timsort, 'b-', lw = 2, label = 'timsort')
plt.loglog(i, sort_set, 'g-', lw = 2, label = 'set_sort')
plt.xlabel('n')
plt.ylabel('time [ns]')
plt.legend()
plt.show()