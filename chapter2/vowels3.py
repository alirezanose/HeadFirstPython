vowels = ['a', 'e', 'i', 'o', 'u']

word = input("input a word to search for vewels: ")

found = []

for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowel in found:
    print(vowel)
