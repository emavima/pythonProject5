lst = ['flower', 'float', 'flannel']

def longest_common_prefix_1(s):

    occ = ''
    dct = {}

    for word in s:

        for char in word:
            if char in dct:
                dct[char] += 1
            else:
                dct[char] = 1

    for key, values in dct.items():
        if values == len(s):
            occ += key


    return occ

#print(longest_common_prefix(lst))


def longest_common_prefix_2(s):

    i = 0
    if len(s) == 0:
        return None
    for char in s[0]:
        for word in s[1:]:
            if word[i] != char:
                return word[:i]
        i += 1

    return s[0]

print(longest_common_prefix_2(lst))