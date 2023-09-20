def sum_divisors(number):
    divisor = 1
    total = 0
    
    if number < 1:
        return 0
    while True:
        if number % divisor == 0:
            total += divisor
            divisor += 1
            print(divisor)
    return total
    
#print(sum_divisors(0))
#print(sum_divisors(3))
print(sum_divisors(36))
print(sum_divisors(102))

    