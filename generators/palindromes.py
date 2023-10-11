# TODO: генерация палиндром (слов, читающихся одинаково с начала и с конца)

import random
import string


def generate_palindromes(length, count):
    result = []
    for i in range(count):
        if length % 2 == 0:
            result_str = ''.join(random.choice(string.ascii_lowercase) for i in range(int(length/2)))
            result.append(result_str + result_str[::-1])
        else:
            result_str = ''.join(random.choice(string.ascii_lowercase) for i in range(int((length-1)/2)))
            result.append(result_str + random.choice(string.ascii_lowercase) + result_str[::-1])
    return result


def generate_palindromes_generator(length):

    while True:
        if length % 2 == 0:
            result_str = ''.join(random.choice(string.ascii_lowercase) for i in range(int(length/2)))
            yield result_str + result_str[::-1]
        else:
            result_str = ''.join(random.choice(string.ascii_lowercase) for i in range(int((length-1)/2)))
            yield result_str + random.choice(string.ascii_lowercase) + result_str[::-1]

        

print("Generate palindrome with length 10")
print(generate_palindromes(10, 10))

print("Generate 10 palindrome with length 10 using generators")
gpg = generate_palindromes_generator(10)
for i in range(10):
    print(next(gpg))
