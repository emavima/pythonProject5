lst = [5, 9, 3, 7, 1, 9]

def second_largest(lst):

    max_value = max(lst)

    for char in lst:
        if char == max_value:
            lst.remove(char)

    return max(lst)

print(second_largest(lst))