import math
for i in range(2**50, 2**56, 73364):
    if int(math.log2(i)) != i.bit_length()-1:
        print(i, int(math.log2(i)), i.bit_length()-1)
print("END")