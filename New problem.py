s = 'hello'

def first_non_repeated_char(s):


    i = 0
    dct = {}
    non_repeated = ''


    for char in s:
        if char in dct:
            dct[char] += 1
        else:
            dct[char] = 1

    for key, value in dct.items():
        if value == 1:
            non_repeated += key



    return non_repeated[0]

print(first_non_repeated_char(s))