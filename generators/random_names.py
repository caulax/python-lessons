# Реализуйте генератор, который возвращает случайные имена и фамилии.

import names
import random


def generate_random_names(count):
    names = ['Bridget', 'Jennifer', 'George', 'Gary', 'Andrea', 'Terry', 'Stephania', 'Harriette', 'Holly', 'Felix']
    surnames = ['Holloway', 'Dowdy', 'Trost', 'Muterspaw', 'Hancock', 'Bell', 'Medin', 'Dykstr', 'Morris', 'Field']
    result = []
    for i in range(count):
        result.append(f"{random.choice(names)} {random.choice(surnames)}")
    return result

def generate_random_names_infinite(count):
    result = []
    for i in range(count):
        result.append(names.get_full_name())
    return result


def generate_random_names_generator():
    names = ['Bridget', 'Jennifer', 'George', 'Gary', 'Andrea', 'Terry', 'Stephania', 'Harriette', 'Holly', 'Felix']
    surnames = ['Holloway', 'Dowdy', 'Trost', 'Muterspaw', 'Hancock', 'Bell', 'Medin', 'Dykstr', 'Morris', 'Field']
    while True:
        yield f"{random.choice(names)} {random.choice(surnames)}"

def generate_random_names_infinite_generator():
    while True:
        yield names.get_full_name()


# run functions

print("Get 10 random names")
print(generate_random_names(10))

print("Get 10 infinite random names")
print(generate_random_names_infinite(10))

print("Get 10 random names with generators")
random_name = generate_random_names_generator()
for i in range(10):
    print(next(random_name))

print("Get 10 infinite random names with generators")
random_name_g = generate_random_names_infinite_generator()
for i in range(10):
    print(next(random_name_g))
