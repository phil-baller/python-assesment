def is_power_of_two(number):
    while number % 2 == 0:
        number = number / 2
        if number / 2 < 1:
            break
    if number == 1:
        return True
    else:
        return False

print(is_power_of_two(0))
print(is_power_of_two(1))
print(is_power_of_two(8))
print(is_power_of_two(9))
                
            
            