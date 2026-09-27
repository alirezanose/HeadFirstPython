vowels = ['a', 'e', 'i', 'o', 'u']

word = "Miliways Ahmad ali reza"

found = []

print(len(found))

found.append('a')

print(len(found))

for letter in word:
    if letter in vowels:
        print(letter)
