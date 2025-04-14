def collatz_seq(n):
    collatz_seq = []
    while n!=1:
        if n%2 == 0:
            n = n/2
            collatz_seq.append(n)
        else:
            n = (3*n)+1
            collatz_seq.append(n)
    return len(collatz_seq)

lengths = []
nums = []
for i in range(1000001,1,-1):
    length = collatz_seq(i)
    lengths.append(length)
    nums.append(i)

largest_length_idx = lengths.index(max(lengths))
num = nums.index(largest_length_idx)

print(num)




