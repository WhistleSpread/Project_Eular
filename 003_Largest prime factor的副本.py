#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 20:01:58 2018

@author: gongmike
"""

import math
 
def maxPrimeFactors (n):
     
    maxPrime = -1
     
    while n % 2 == 0:
        maxPrime = 2
        n >>= 1  # equivalent to n /= 2
        
    print 'n =', n # 找到了最大的奇数，因为最大是素数一定是最大奇数的因数；
    # 有了这一步，计算量缩小了不少；

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        # 从3 到 int(math.sqrt(n)) + 1 之间所有的奇数都可能是因子；
        while n % i == 0:
            # 当这个数是素数因子的时候；
            maxPrime = i
            print 'maxPrime =', maxPrime
            n = n / i
            # 因为素数的性质就是除了1和自身以外，没有其他因子；
            print 'n =', n


    if n > 2:
        maxPrime = n
     
    return int(maxPrime)
 
n = 13195
print maxPrimeFactors(n)
 
#n = 25698751364526
#print maxPrimeFactors(n)

n = 600851475143
print maxPrimeFactors(n)