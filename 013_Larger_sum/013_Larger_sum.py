#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 12:48:42 2018

@author: gongmike
"""

#nums = []
#with open('number.txt', 'r') as f:
#    for num in f:
#        nums.append(int(float(num)))
#
#print 'nums =', nums

def foo():
    datasum = 0
    with open ("number.txt", "r") as myfile:
        for num in myfile:
            num = num.replace('\n', '')
            datasum += int(float(num))
    return datasum