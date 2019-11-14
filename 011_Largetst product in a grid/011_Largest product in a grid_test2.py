#encoding = utf-8

import os

N = 20

matrix = []
file = open("./011.txt", 'r')
for i in range(20):
	line = file.readline()[:-1]
	array = line.split(' ')
	array = [int(i) for i in array]
	matrix.append(array)

max_val = 0

for i in range(17):
	for j in range(17):
		row_max = matrix[i][j]*matrix[i][j+1]*matrix[i][j+2]*matrix[i][j+3]
		col_max = matrix[j][i]*matrix[j+1][i]*matrix[j+2][i]*matrix[j+3][i]
		main_dia_upp_max = matrix[i][j]*matrix[i+1][j+1]*matrix[i+2][j+2]*matrix[i+3][j+3]
		sec_dia_max = matrix[i][N-j-1]*matrix[i+1][N-j-2]*matrix[i+2][N-j-3]*matrix[i+3][N-j-4]
		max_val = max(max_val, max(row_max, col_max, main_dia_max, sec_dia_max))

print('max_val = ', max_val)