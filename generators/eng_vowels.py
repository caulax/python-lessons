# TODO: Создайте генератор, который возвращает все английские гласные буквы
def get_all_eng_vowels():
    all_vowels = ['a', 'e', 'i', 'o', 'u']
    return all_vowels

def get_all_eng_vowels_generator():
    all_vowels = ['a', 'e', 'i', 'o', 'u']
    for i in all_vowels:
        yield i
        

print("Get all english vowels")
print(get_all_eng_vowels())

print("Get all english vowels using generators")
eng_vowels = get_all_eng_vowels_generator()
for g in eng_vowels:
    print(g)
