import math

n = 20000
nums = [i for i in range(1,n+1)]
triangle_nums = []
count = []

for i in range(1,len(nums)):
    triangle_nums.append(sum(nums[:i]))

def count_divisors(num):
    divisors = set()
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            divisors.add(i)
            divisors.add(num // i)
    return len(divisors)

for t in triangle_nums:
    count.append(count_divisors(t))

filtered = list(filter(lambda x:x>500, count))[0]
idx = count.index(filtered)
print(triangle_nums[idx])