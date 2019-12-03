import random, time
from randcrack import RandCrack

random.seed(0)
first_random_is = "{0:b}".format(random.randrange(16 ** 32))

random_bits_string = first_random_is
while len(random_bits_string) <= (624 * 32):
    random_bits_string = "{0:b}".format(random.randrange(0, 16 ** 32)) + random_bits_string # 128~ bits each round

print("Total random bits generated: ",len(random_bits_string),", ",len(random_bits_string) -  (624 * 32), "More than needed" )

bit32_random_array = []
while len(random_bits_string) >= 32:
    bit32_random_array.append(bin(int(random_bits_string[-32:],2)))
    random_bits_string = random_bits_string[:-32]
bit32_random_array.append(bin(int(random_bits_string,2)))

print(bit32_random_array)

rc = RandCrack()
for i in range(624):
    print("Submiting", bin(int(bit32_random_array[i],2)))
    rc.submit(int(bit32_random_array[i],2))
    bit32_random_array[i] = ""

bit32_random_array = list(filter(None,bit32_random_array))
print(bit32_random_array)
