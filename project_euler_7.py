import sympy as sp

list_prime = []
for i in range(1,1000000):
    if sp.isprime(i):
        list_prime.append(i)

print(list_prime[10000])