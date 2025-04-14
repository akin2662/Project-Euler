def power_digit_sum(n):
    num = 2**n
    string_num = str(num)
    string_num = string_num.replace("", " ")
    string_num = string_num.split()
    digits = [int(i) for i in string_num]
    return sum(digits)

n = 15
print(power_digit_sum(1000))