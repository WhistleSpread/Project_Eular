#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 09:53:08 2018

@author: gongmike
"""
import time 

# 在程序开始执行的时候记录一下开始的时间，
startTime = time.time()
for a in range(1001):
    for b in range(1001):
        c = 1000-a-b
        if c**2 == a**2 + b**2:
            print 'a =', a, 'b =', b, 'c= ', c
endTime = time.time()

print "times = ", endTime - startTime