#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 09:04:48 2018

@author: gongmike
"""
import math

def isPrime(i):
    s = int(math.sqrt(i))
#    print 's =',s
    if i % 2 != 0:
        for k in range(3, s+1, 2):
#            print 'now k = ', k
            if i%k == 0:
                return False
        return True
    else:
        return False

natural = 2
count = 1
while(True):
    natural += 1
    if isPrime(natural):
        count += 1
    if count == 10001:
        break

print 'the 10 001st prime number is ', natural

    