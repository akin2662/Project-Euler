def is_palindrome(num):
    string_num = str(num)
    reverse = string_num[::-1]
    if string_num == reverse:
        return True
    else:
        return False

palindromes = []
for i in range(99,1000):
    for j in range(100,999):
        product = i*j
        if is_palindrome(product):
            palindromes.append(product)

print(max(palindromes))



