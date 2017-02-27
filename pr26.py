def sum_of_natural(num):
    if (num==0):
        return 0
    sum = num + sum_of_natural(num - 1)
    return sum

def factorial(num):
    if (num==0):
        return 1
    sum = num * factorial(num - 1)
    return sum


print(sum_of_natural(10))
print(factorial(5))

