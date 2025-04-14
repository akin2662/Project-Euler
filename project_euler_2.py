term1 = 1
term2 = 2
next_num = 0
fib = [term1,term2]
while next_num<4000000:
    next_num = term2 +term1
    term1 = term2
    term2 = next_num
    fib.append(next_num)

even_num = list(filter(lambda x: x%2 ==0 , fib))
print(sum(even_num))