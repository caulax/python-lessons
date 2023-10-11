# TODO: Використовуйте генератор для генерації букв алфавіту

def alphabet_generator():
    current_letter = 'a'
    while True:
        yield current_letter
        current_letter = chr(ord(current_letter) + 1)
        if current_letter > 'z':
            break

print("Get all letters from english alphabet using generators")
letters = alphabet_generator()
for letter in letters:
    print(letter)
