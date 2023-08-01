lst = [1, 2, 4, 12, 3, 6, 8, 9, 10, 11, 5, 13, 14, 16, 7]

def find_missing_number(lst):


    lst.sort()
    n = len(lst)
    exp = n+1

    total = sum(lst)

    expected_sum = exp * (exp + 1) // 2

    missing_num = expected_sum - total

    return missing_num

print(find_missing_number(lst))