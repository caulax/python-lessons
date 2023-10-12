# TODO: Реализуйте генератор, который выдает случайные пароли.

import random
import string

def passwords(number_of_sym: int):
    symbols = string.ascii_letters + string.punctuation + string.digits
    while True:
        # password = ''
        # for _ in range(number_of_sym):
        #     password += random.choice(symbols)
        # yield password
        yield ''.join(random.choice(symbols) for _ in range(number_of_sym))

iter_result = passwords(10)
for a in range(10):
    print(next(iter_result))
