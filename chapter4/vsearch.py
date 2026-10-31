def search4vowels(word):
    """Display any vowels found in a string"""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)

search4vowels('ahmad ali reza')
