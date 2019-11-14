#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 10:50:32 2018

@author: gongmike
"""
# 说实话，我感觉这个方法并不好，可是没有想到好的方法，这个就是遍历出来的，太慢了；

import math

def odd_is_prime(i):
    divisor = 3
    while divisor <= math.sqrt(i):
        if i % divisor != 0:
            divisor += 2
        else:
            return False
    return True
    

line = 2000000
prime_list = []

i = 3
while i < 2000000:
    if odd_is_prime(i):
        print 'i =', i
        prime_list.append(i)
    i += 2

print 'sum =', sum(prime_list) + 2
    