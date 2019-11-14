import math 

def proper_divisors(n):
    result = [1]
    d = 2
    while d <= math.sqrt(n):
        if n % d == 0:
            result.append(d)
            result.append(n // d)
        d = d + 1
    return result

def sum_list(list):
    sum = 0
    for i in list:
        sum += i
    return sum

pair_dict = {}
amicable_pair = []

def d(n):
    return sum_list(proper_divisors(n))

def amicable_pair_value(m, n):
    if d(m) == n and d(n) == m and m != n:
        return True
    return False 


for i in range(2, 10000, 1):
    if i not in pair_dict.keys():
        pair_dict[i] = d(i)
        pair_dict[pair_dict[i]] = d(pair_dict[i])
        if amicable_pair_value(i, pair_dict[i]):
            amicable_pair.append((i, pair_dict[i]))

# print("pair_dict = ", pair_dict)
print("amicable_pair = ", amicable_pair)

sum = 0
for pair in amicable_pair:
    sum += pair[0] + pair[1]
    
print("sum = ", sum)




    