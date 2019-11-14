#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 12:16:43 2018

@author: gongmike
"""

def isPalindrome(n):
    s = str(n)
    if s == s[::-1]:
        return True
    else:
        return False
    
def isProductOfThree(n):
    for i in range(100, 1000, 1):
        if n % i == 0 and len(str(n/i))==3:
            return True

#print isPalindrome(9009)
# 999* 999 =998001
        
for i in range(998001, 0, -1):
    print i
    if isPalindrome(i):
        print i, 'is a palindrome'
        if isProductOfThree(i):
            print i, 'is a product of two 3-digits'
            break
        

#for i in range(0, 998001, 1):
#    if isPalindrome(i):
#        print i, 'is a palindrome'
#
#def isProductOfThree(n):
#    for i in range(100, 1000, 1):
#        if n % i == 0 and len(str(n/i))==3:
#            return True