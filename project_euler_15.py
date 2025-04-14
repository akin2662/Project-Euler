import math

# Calculate the number of unique permutations
n = 40  # Total elements
k = 20  # Repeated elements for both 'move_rights' and 'move_downs'

# Formula: Unique Permutations = 40! / (20! * 20!)
unique_permutations = math.factorial(n) // (math.factorial(k) ** 2)

print(unique_permutations)



