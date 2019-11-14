#encoding = utf-8

import os

matrix = []
file = open("./011.txt", 'r')
for i in range(20):
	line = file.readline()[:-1]
	array = line.split(' ')
	array = [int(i) for i in array]
	# print('array = ', array)
	matrix.append(array)

# print('matrix = ', matrix)

def max_of_lines(matrix):
	max_of_line_list = []
	for i in range(20):
		cur_product = matrix[i][0]*matrix[i][1]*matrix[i][2]*matrix[i][3]
		# print('cur_product = ', cur_product)
		max_of_line = cur_product
		for j in range(16):
			if(cur_product != 0 and matrix[i][j] != 0):
				cur_product = cur_product//matrix[i][j]*matrix[i][j+4]
			else:
				j = j+4
				cur_product = matrix[i][j]*matrix[i][j+1]*matrix[i][j+2]*matrix[i][j+3]
			# print('cur_product = ', cur_product)
		if(cur_product > max_of_line):
			max_of_line = cur_product
		max_of_line_list.append(max_of_line)
	return max_of_line_list


def max_of_cols(matrix):
	max_of_col_list = []
	for j in range(20):
		cur_product = matrix[0][j]*matrix[1][j]*matrix[2][j]*matrix[3][j]
		# print('cur_product = ', cur_product)
		max_of_col = cur_product
		for i in range(16):
			if(cur_product != 0 and matrix[i][j] != 0):
				cur_product = cur_product//matrix[i][j]*matrix[i+4][j]
			else:
				i = i+4
				cur_product = matrix[i][j]*matrix[i+1][j]*matrix[i+2][j]*matrix[i+3][j]
			# print('cur_product = ', cur_product)
		if(cur_product > max_of_col):
			max_of_col = cur_product
		max_of_col_list.append(max_of_col)
	return max_of_col_list

def max_of_pos_tri(matrix):
	max_product = matrix[0][0]*matrix[1][1]*matrix[2][2]*matrix[3][3] 
	cur_product = max_product
	for i in range(16):
		if(cur_product != 0 and matrix[i][i] != 0):
			cur_product = cur_product//matrix[i][i]*matrix[i+4][i+4]
		else:
			while(cur_product == 0):
				i += 1
				cur_product = matrix[i][i]*matrix[i+1][i+1]*matrix[i+2][i+2]*matrix[i+3][i+3]
		if(cur_product > max_product):
			max_product = cur_product
	return max_product

def max_of_neg_tri(matrix):
	max_product = matrix[0][19]*matrix[1][18]*matrix[2][17]*matrix[3][16]
	cur_product = max_product
	for i in range(16):
		if(cur_product != 0 and matrix[i][i] != 0):
			cur_product = cur_product//matrix[i][i]*matrix[i+4][i+4]
		else:
			while(cur_product == 0):
				i += 1
				cur_product = matrix[i][19-i]*matrix[i+1][19-(i+1)]*matrix[i+2][19-(i+2)]*matrix[i+3][19-(i+3)]
		if(cur_product > max_product):
			max_product = cur_product
	return max_product


def max_of_pos_upp_tri(matrix):
	"""对角线之上，右上到左下"""
	max_of_pos_upp_tri_list = []
	max_product = 0
	for i in range(3,20):
		k = i
		for j in range(i):
			cur_product = matrix[i][0]*matrix[i-1][1]*matrix[i-2][2]*matrix[i-3][3]
			if(cur_product != 0):
				cur_product = cur_product//matrix[i][j]*matrix[i-4][j+4]
			else:
				while(cur_product == 0):
					j += 1
					cur_product = matrix[i-j][j]*matrix[i-j-1][j+1]*matrix[i-j-2][j+2]*matrix[i-j-3][j+3]
			if(cur_product > max_product):
				max_product = cur_product

	return max_product
		
		

	return max_of_pos_upp_tri_list
def max_of_pos_upp_tri2(matrix):
	"""对角线之下，右上到左下"""
	for row in range(3, 36):
		for j in range(i)









max_of_pos_upp_tri(matrix)
# print('max_of_col_list = ', max_of_lines(matrix))
# print('max_of_col_list = ', max_of_cols(matrix))
# print('max_of_pos_tri = ', max_of_pos_tri(matrix))
# print('max_of_neg_tri = ', max_of_neg_tri(matrix))



