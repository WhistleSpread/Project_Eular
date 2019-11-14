def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

a = factorial(100)
sum = 0
while a != 0:
    sum += a % 10
    a = a // 10
print("sum = ", sum)
print("a = ", a) 