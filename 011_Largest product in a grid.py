#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 11:17:01 2018

@author: gongmike
"""

N = 20
n = 4
line = N - n + 1

l1 = [8, 2, 22,97,38,15, 0,40, 0,75, 4, 5, 7,78,52,12,50,77,91,8]
l2 = [49,49,99,40,17,81,18,57,60,87,17,40,98,43,69,48, 4,56,62,0]
l3 = [81,49,31,73,55,79,14,29,93,71,40,67,53,88,30, 3,49,13,36,65]
l4 = [52,70,95,23, 4,60,11,42,69,24,68,56, 1,32,56,71,37, 2,36,91]
l5 = [22,31,16,71,51,67,63,89,41,92,36,54,22,40,40,28,66,33,13,80]
l6 = [24,47,32,60,99, 3,45, 2,44,75,33,53,78,36,84,20,35,17,12,50]
l7 = [32,98,81,28,64,23,67,10,26,38,40,67,59,54,70,66,18,38,64,70]
l8 = [67,26,20,68, 2,62,12,20,95,63,94,39,63, 8,40,91,66,49,94,21]
l9 = [24,55,58, 5,66,73,99,26,97,17,78,78,96,83,14,88,34,89,63,72]
l10 = [21,36,23, 9,75, 0,76,44,20,45,35,14, 0,61,33,97,34,31,33,95]
l11 = [78,17,53,28,22,75,31,67,15,94, 3,80, 4,62,16,14, 9,53,56,92]
l12 = [16,39, 5,42,96,35,31,47,55,58,88,24, 0,17,54,24,36,29,85,57]
l13 = [86,56, 0,48,35,71,89, 7, 5,44,44,37,44,60,21,58,51,54,17,58]
l14 = [19,80,81,68, 5,94,47,69,28,73,92,13,86,52,17,77, 4,89,55,40]
l15 = [ 4,52, 8,83,97,35,99,16, 7,97,57,32,16,26,26,79,33,27,98,66]
l16 = [88,36,68,87,57,62,20,72, 3,46,33,67,46,55,12,32,63,93,53,69]
l17 = [ 4,42,16,73,38,25,39,11,24,94,72,18, 8,46,29,32,40,62,76,36]
l18 = [20,69,36,41,72,30,23,88,34,62,99,69,82,67,59,85,74, 4,36,16]
l19 = [20,73,35,29,78,31,90, 1,74,31,49,71,48,86,81,16,23,57, 5,54]
l20 = [ 1,70,54,71,83,51,54,69,16,92,33,48,61,43,52, 1,89,19,67,48]

matrix = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14, l15, l16, l17, l18, l19, l20]
cal_n_matrix = []

larger_product_list = []

def product_of_cal_matrix(cal_n_matrix):
    product_list = []
    for i in range(4):
        product = 1
        for j in range(4):
#            print 'product = ', product, '*', cal_n_matrix[i][j]
            product *= cal_n_matrix[i][j]
        product_list.append(product)
#        print 'product_list =', product_list
            

    for j in range(4):
        product = 1
        for i in range(4):
#            print 'product = ', product, '*', cal_n_matrix[i][j]
            product *= cal_n_matrix[i][j]
        product_list.append(product)
#        print 'product_list =', product_list
    
    product = 1
    for i in range(4):
        product *= cal_n_matrix[i][i]
    product_list.append(product)
    
    product = 1
    for i in range(4):
        for j in range(4):
            if i+j == 3:
                product *= cal_n_matrix[i][i]
    product_list.append(product)
    
    print 'product_list =', product_list
    return max(product_list)
                

for i in range(line):
    for j in range(line):
        a = matrix[i][j:j+4]
        b = matrix[i+1][j:j+4]
        c = matrix[i+2][j:j+4]
        d = matrix[i+3][j:j+4]
        cal_n_matrix = [a, b, c, d]
#        print 'cal_n_matrix =', cal_n_matrix
#        print 'product_of_cal_matrix(cal_n_matrix) =', product_of_cal_matrix(cal_n_matrix)
        print '=========================================================================='
        larger_product_list.append(product_of_cal_matrix(cal_n_matrix))

#print 'larger_product_list =', larger_product_list
print 'max =', max(larger_product_list)
    
        
        
