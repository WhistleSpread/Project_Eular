#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 08:56:48 2018

@author: gongmike
"""

def sum_of_squares(num):
    tot = 0
    for i in range(num+1):
        tot += i**2
    return tot

def squares_of_sums(num):
    tot = (1+num)*num/2
    return tot**2