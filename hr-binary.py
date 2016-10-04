n = int(input().strip())
binary_s = bin(n)[2:]

num_ones = 0
max_ones = 0
for bit in binary_s:
    if int(bit) == 1:
        num_ones += 1
        if num_ones > max_ones:
            max_ones = num_ones
    else:
        num_ones = 0

print(max_ones)
