#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 12:07:07 2018

@author: gongmike
"""
# 这个用递归来做比较好；

import math
import time

t1 = time.time()
def count_divisors(n):
    count = 0
    for i in range(1, int(math.sqrt(n+1))):
        if n % i == 0:
            count += 1
    return 2*count

th = 1
tri_num = 1
counts = 1

while counts < 500:
    print 'tri_num =', tri_num
    counts = count_divisors(tri_num)
    print 'count divisors =', counts
    if counts >= 500:
        break
    else:
        th += 1
        tri_num += th
    
print 'tri_number =', tri_num

t2 = time.time()

print 'T =', t2 - t1
#T = 27.8668780327
