#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 11:23:46 2018

@author: gongmike
"""
#
#def divisible(n,t):
#    for i in range(1, t, 1):
#        if n % i != 0:
#            return False
#    return True



#def divisible(n):
#    i = 12
#    while i < 21:
#       if n % i != 0:
#           return False
#       else:
#           i += 2
#    return True
#
#n = 2520*11*13*17*19
#
#while True:
#    if divisible(n):
#        print n, 'is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20'
#        break
#    else:
#        n += 2
#        print 'n =', n
        
        

#
#def divisible(n):
#    i = 1
#    while i < 10:
#       if n % i != 0:
#           return False
#       else:
#           i += 1
#    return True
#
#n = 20
#while True:
#    if divisible(n):
#        print 
#        print n, 'is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20'
#        break
#    else:
#        n += 1
        
#fact = 1       
#for i in range(9, 20, 1):
#    fact *= i
#    print 'fact =', fact
        

#def cbdl(n, i):
#    for i in range(i, 21, 1):
#        if n % i != 0:
#            return False
#    return True
#
#i = 11
#n = 2520        
#while True:
#    if cbdl(n, i):
#        print n
#        break
#    else:
#        i += 1
#        print 'i =', i
#        n = n * i
#        print 'n =', n


if 2520%11 != 0:
    n = 2520/11
    n += 1
    while (n*11) % 12 != 0:
        n +=1
    candi = n * 11
if candi % 13 != 0:
    n = candi/13







def rfac(n):
    multi = 1
    for i in range(11, n+1, 1):
#        print 'i =', i
        multi *= i
#        print 'multi =', multi
    return multi

candidate = 2520    
for i in range(11, 21, 2):
    print 'candidate % rfac(i) = ', candidate % rfac(i)
    if candidate % rfac(i) != 0:
        n = candidate/rfac(i)
        n += 1
        while (n*rfac(i)) % (i+1) != 0:
            n += 1
        print 'n*rfac(i) =', n, '*', rfac(i) , '=', n*rfac(i)
        candidate = (((n*i)/rfac(i+1))+1) * rfac(i+1)
        print 'candidate =', candidate
             
        
print 'candidate =', candidate

print(reduce(lambda x,y:x*y,[9,5,7,11,13,16,17,19],1))










































