import math

def lcm_of_list(numbers):
    lcm = numbers[0]
    for num in numbers[1:]:
        lcm = (lcm * num) // math.gcd(lcm, num)
    return lcm

numbers = list(range(1, 21))  # Numbers from 1 to 10
result = lcm_of_list(numbers)
print(result)
