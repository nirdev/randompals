#!/bin/python3.6
import random
def generate_new_token():
    return f'{random.randrange(16 ** 32):08x}'

if __name__ == '__main__':
    print (generate_new_token())