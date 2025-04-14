# Used euclids formula for generating triplets:
# a = m**2 - n**2
# b = 2*m*n
# c = m**2 + n**2

#Therefore a+b+c = 2*m**2 + 2*m*n = 1000; m**2 + m*n = 500; m*(m+n) = 500

list_of_integer_pairs = []
for i in range(1,500):
    for j in range(1,500):
        if j*(j+i) == 500:
            list_of_integer_pairs.append((j,i))

triplets = []
for i in list_of_integer_pairs:
    a = i[0]**2 - i[1]**2
    b = 2*i[0]*i[1]
    c = i[0]**2 + i[1]**2
    triplets.append((a,b,c))

for i in triplets:
    if i[0]>0 and i[1]>0 and i[2]>0:
        if i[0]+i[1]+i[2] == 1000:
            print(i[0]*i[1]*i[2])


