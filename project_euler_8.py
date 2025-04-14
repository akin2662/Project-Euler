def filter(num):
    no_zeros_list = []
    for i in range(len(num) - 12):  # Ensure that we always have a window of 13 digits
        window = num[i:i + 13]
        if '0' in window:
            continue  # Skip windows that contain zero
        no_zeros_list.append(window)
    return no_zeros_list

def find_largest_prod(num):
    no_zeros_list = filter(num)  # Get valid 13-digit windows without zeros
    prod_list = []
    for i in no_zeros_list:
        ref = 1
        list_nums = list(map(int, i))  # Convert characters in the window to integers
        for val in list_nums:
            ref *= val  # Multiply all digits in the window
        prod_list.append(ref)

    if prod_list:  # Check if the list is not empty
        return max(prod_list)
    else:
        return None  # No valid products found


# List of numbers (represented as strings for the very large numbers)
num = [
    '73167176531330624919225119674426574742355349194934',
    '96983520312774506326239578318016984801869478851843',
    '85861560789112949495459501737958331952853208805511',
    '12540698747158523863050715693290963295227443043557',
    '66896648950445244523161731856403098711121722383113',
    '62229893423380308135336276614282806444486645238749',
    '30358907296290491560440772390713810515859307960866',
    '70172427121883998797908792274921901699720888093776',
    '65727333001053367881220235421809751254540594752243',
    '52584907711670556013604839586446706324415722155397',
    '53697817977846174064955149290862569321978468622482',
    '83972241375657056057490261407972968652414535100474',
    '82166370484403199890008895243450658541227588666881',
    '16427171479924442928230863465674813919123162824586',
    '17866458359124566529476545682848912883142607690042',
    '24219022671055626321111109370544217506941658960408',
    '07198403850962455444362981230987879927244284909188',
    '84580156166097919133875499200524063689912560717606',
    '05886116467109405077541002256983155200055935729725',
    '71636269561882670428252483600823257530420752963450']

# Finding the largest product
largest_prods = []
for i in num:
    large = find_largest_prod(i)
    if large is not None:
        largest_prods.append(large)

print(largest_prods)

print(max(largest_prods))  # Output the largest product found
