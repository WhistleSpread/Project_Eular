#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 30 09:03:34 2018

@author: gongmike
"""
#
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
import math

number =  600851475143
#number = 13195
# 其实判断是不是素数有三种方法，第一种就是遍历，不过不需要全部都遍历，只需要遍历到sqrt(n)即可；
#因为如果存在因子的话，最大不会超过sqrt（n）因为要相乘啊；
# 判断素数的第二种方法：判断2之后，就可以判断3到sqrt(n)之间的奇数，不用再考虑之间的偶数了；
#def isPrime(i):
#    s = int(math.sqrt(i))
#    for k in range(2, s):
#        if s % k == 0:
#            return False
#    return True

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

while number % 2 ==0:
    number /= 2

prime_list = []
n = 3
while n < number:
    if number % n == 0 and isPrime(n):
        prime_list.append(n)
    n += 2

print 'the_largest_prime =', max(prime_list)




