# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 16:41:04 2020

@author: rowe1
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 14:42:35 2020

@author: rowe1
"""

import time
import matplotlib.pyplot as plt
import random
import collections

i = [10**j for j in range(3, 7)]

list_set = []
timsort = []
for j in i:
    a = list(range(1, j))
    random.shuffle(a)
    
    # timsort
    t0 = time.time_ns()
    sorted(a)
    timsort.append(time.time_ns() - t0)
    
    
    # list set sort
    t0 = time.time_ns()
    #c = collections.Counter(a)
    #b = sorted(c)
    list(set(a))
    
    #k = 0
    #for num in b:
    #    a[k:k+c[num]] = [num]*c[num]
    #    k += c[num]
    list_set.append(time.time_ns() - t0)

plt.close('all')
plt.figure()
plt.loglog(i, list_set, 'r-', lw = 2, label = 'list_set')
plt.loglog(i, timsort, 'b-', lw = 2, label = 'timsort')
plt.xlabel('n')
plt.ylabel('time [ns]')
plt.legend()
plt.show()