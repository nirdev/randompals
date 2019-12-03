import random, time
from randcrack import RandCrack


#
# for i in range(624):
# 	rc.submit(random.getrandbits(32))
# 	# Could be filled with random.randint(0,4294967294) or random.randrange(0,4294967294)
#
# print("Random result: {}\nCracker result: {}"
# 	.format(random.randrange(16 ** 32), rc.predict_randrange(16 ** 32)))

# 3279748397
#

random.seed(0)
first_random_is = "{0:b}".format(random.randrange(16 ** 32))

random_bits_string = first_random_is
while len(random_bits_string) <= (624 * 32):
    random_bits_string = "{0:b}".format(random.randrange(0, 16 ** 32)) + random_bits_string # 128 bits each round


print("Number of random bits is = ", len(random_bits_string))
print("LEN IS:",len(first_random_is))
print(first_random_is)
print(bin(int(first_random_is,2)))
print(random_bits_string)
# random_bits = bin(int(random_bits_string,2))
# print(random_bits)


# first32 = random_bits[len(random_bits) - 32:]
bit32_random_array = []
while len(random_bits_string) >= 32:
    bit32_random_array.append(bin(int(random_bits_string[- 32:],2)))
    random_bits_string = random_bits_string[:-32]

rc = RandCrack()
for i in range(624):
    rc.submit(random_bits_string[i])
    random_bits_string[i] = 0



    # print(i)
# print(bit32_random_array)
# print(len(bit32_random_array))


# 0b11100011111001110000011010000010110000100000100101001100101011000110001010011111011011111011111011011000001011000000011111001101
#

# >>> random.seed(0)
# '0b11011000001011000000011111001101' 1
# '0b1100010100111110110111110111110' 2
# '0b11000010000010010100110010101100' 3
# '0b11100011111001110000011010000010' 4
# '0b1101011101010101001010001010101' 5
# '0b1010010111010010111100110100'
# >>> bin(random.getrandbits(32))
# '0b1000010010010000101111000111010'
# >>> bin(random.getrandbits(32))
# '0b11110111001010001011010011111010'
# >>> bin(random.getrandbits(32))
# '0b10000010111000101110011001100010'
# >>> bin(random.getrandbits(32))
# '0b1111100011001011100000111100101'
# >>> bin(random.getrandbits(32))
# '0b1100111101010011100001101111000'
# >>> bin(random.getrandbits(32))
# '0b11101011000100010110011110110011'
# >>> bin(random.getrandbits(32))
# '0b11001000101001110000011000111001'
# >>> bin(random.getrandbits(32))
# '0b11010100011100010011110101100000'
# >>>
