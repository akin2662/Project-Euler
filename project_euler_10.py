import sympy as sp

nums = list(range(1,2000001))
prime = []
for i in nums:
    if sp.isprime(i):
        prime.append(i)

print(sum(prime))