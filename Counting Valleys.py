inp = "DDUDUUDU"

def counting_valleys(inp):

    valleys_crossed = 0
    sea_level = 0


    for char in inp:

        if char == 'U':
            sea_level += 1
        elif char == 'D':
            sea_level -= 1
        if sea_level == 0:
            valleys_crossed += 1







    return valleys_crossed


print(counting_valleys(inp))
