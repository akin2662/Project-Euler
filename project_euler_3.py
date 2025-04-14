import sympy as sp

num = 600851475143
n = num
prime_factors = []

# Start with 2 (the smallest prime)
i = 2
while i * i <= n:
    if n % i == 0:
        prime_factors.append(i)
        n = n // i  # Divide out the factor completely
    else:
        i += 1 if i == 2 else 2  # Check 2, then only odd numbers

# If something > 1 remains, it's also a prime
if n > 1:
    prime_factors.append(n)

print(f"Prime factors of {num} are: {prime_factors}")
print(f"Largest prime factor: {max(prime_factors)}")