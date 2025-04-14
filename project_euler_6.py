n = 100

list_nums = list(range(1,n+1))

squares = list(map(lambda x:x**2,list_nums))
sum_of_squares = sum(squares)
sum_of_nums = sum(list_nums)
square_of_sum = sum_of_nums**2
diff = square_of_sum - sum_of_squares
print(diff)