#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 07:57:24 2018

@author: gongmike
"""
import sys
sys.setrecursionlimit(100000)


#def fibo(n):
#    if n == 1:
#        return 1
#    elif n == 2:
#        return 2
#    else:
#        return fibo(n-1) + fibo(n-2)
#
##def testFibo(n): # and i didn't figure out why it turn out to be runtime error?
##    for i in range(n+1):
##        print 'fibo of', i, '=', fibo(i)
##        
##
##testFibo(1)
#        
##for i in range(10):
##    print 'fib(', i, ') = ', fibo(i)
#        
#print fibo(3)
#print fibo(10)
#print fibo(40) # it costs a while!!
##print fibo(100) # it costs too much time!!!
##print fibo(4000000)

# 一种改进的递归方法：
memo = {0:0, 1:1}
def fibona(n):
    if not n in memo:
        memo[n] = fibona(n-1) + fibona(n-2)
    return memo[n]
for i in range(10):
    print 'fib(', i, ') = ', fibo(i)
# 不过用递归的话，最后还是kernal died；

## 采用迭代而不是递归的方式，可以让程序快不少！
#def fib(n):
#    a, b = 1, 2
#    for i in range(n):
#        a, b = b, a+b
#    return a
##print fib(40) # 这种方法快不少啊！
#
#total = 0
#i = 1
#
#while(fib(i) < 4000000):
#    if fib(i) % 2 == 0:
#        total += fib(i)
#    i += 1
#
#print total
## 4613732
#
## 关于fibonacci 数列目前搜集到的好的解法：利用斐波拉契公式
#from math import sqrt
#def F(n):
#    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))
#
#
## 其实，这种方法和上面的 a, b = b, a+b 的思路是一样的；要会这种元组表达式；
#print('!* Fibonacci Sequence python \n')
#def Fibonacci_Series():
#    x = input('Enter Series length to print fibonacci sequence')
#
#    d,e=0,1
#    a = []
#    a.append(d)
#    a.append(e)
#    while(x!=2):
#        c = d + e
#        d = e
#        e = c
#        a.append(c)
#        x = x -1
#    print(a)

