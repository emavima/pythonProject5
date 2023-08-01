str =  "abcaaccbbeed"

def most_frequent(str):
    dict = {}

    for char in sorted(str.lower()):
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1

    lst = []
    max_key = 0

    for key in dict:

        if dict[key] > max_key:
            max_key = dict[key]
            lst.append(key)
        elif dict[key] == max_key:
            lst.append(key)

    return lst



print(most_frequent(str))

