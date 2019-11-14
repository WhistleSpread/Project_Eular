data_matrix = [None]
data = open("./triangle.txt")
for line in data:
    line = line.split()
    temp = [None]
    for num in line:
        temp.append(int(num))
    data_matrix.append(temp)
data.close

temp_dict = {}

# matrix = [None]
# for list in data_matrix:
#     matrix.append(list)

print("matrix = ", data_matrix)

for i in range(1, 101, 1):
    if i == 1 :
        row_now_index = 100
        row_now = data_matrix[row_now_index]
        
        print(len(row_now))
        for i in range(1, len(row_now), 1):
            # print("i = ", i)
            key = "100" + "-" + str(i)
            # print("key = ", key)
            temp_dict[key] = row_now[i]
        print ("temp_dict = ", temp_dict)
    else:
        # row_now = 14, row_next = 15 14/15; 13/14
        print("i = ", i)
        row_now_index = 101 - i
        row_now = data_matrix[row_now_index] 
        # print("row_now = ", row_now)
        row_next = data_matrix[row_now_index + 1]
        # print("row_next = ", row_next)
        
        candidate_row = row_now_index + 1
        print("candidate_row = ", candidate_row)

        for i in range(1, len(row_now), 1):
            candidate_key_1 = str(candidate_row) + "-" + str(i)
            candidate_key_2 = str(candidate_row) + "-" + str(i + 1)
            print((candidate_key_1, candidate_key_2))
            
            candidate = [temp_dict[candidate_key_1], temp_dict[candidate_key_2]]
            print("candidate = ", candidate)
            key = str(row_now_index) + "-" + str(i)
            print("key = ", key)
            temp_dict[key] = max(row_now[i]+candidate[0] , row_now[i] + candidate[1])
            print("i = ", i, "temp_dict = ", temp_dict)



print("temp_dict = ", temp_dict)