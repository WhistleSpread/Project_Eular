#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 15:29:46 2018

@author: gongmike
"""

maxnum = 1000000

def get_seq_count(num):
    count = 1
    while num != 1:
        if num % 2 == 0:
            num /= 2
            count += 1
        else:
            num = 3*num + 1
            count += 1
    return count 


cache = {1: 1}

def collatz(n):
    path = [n]
    while n not in cache:
        if n % 2:
            n = 3 * n + 1
        else:
            n = n / 2
        path.append(n)
#reversed()函数是返回序列seq的反向访问的迭代子。参数可以是列表，元组，字符串，不改变原对象。
    for i, m in enumerate(reversed(path)):
#enumerate()是python的内置函数,对于一个可迭代的（iterable）/可遍历的对象（如列表、字符串），
#enumerate将其组成一个索引序列，利用它可以同时获得索引和值
#enumerate()返回的是一个enumerate对象
        cache[m] = cache[n] + i
    return cache[path[0]]



def k(upto):
    def collatz(n):
        if n < upto and lst[n] > 0:
            return lst[n]
        if n%2 == 0:
            val = collatz(n/2) + 1
            


# 代码这个代码是看别人写的，学习一下别人写的代码，这个我还看不太懂

from functools import lru_cache

@lru_cache(None)
def coll(num):
    if num == 1:
        return 1

    if num % 2:
        return 1+coll(num*3+1)

    return 1+coll(num/2)

longest = 0
for i in range(1, 1_000_001):
    this = coll(i)
    if this > longest:
        print(i, this)
        longest = this


# 学习这段代码，要用到动态规划的思想；
# 也即是已经算过了的不用再算了；
          
            
            
            
            
            
            
            
            
            