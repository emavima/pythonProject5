
inp = 'aipolufe'

def vowel_finder(str):

    vowels = 'aeiou'
    found_vowels = []
    for chars in str:

        if chars in vowels:
            found_vowels.append(chars)


    return len(found_vowels)





print(vowel_finder(inp))