inp = "DDUDUUDU"

def counting_valleys(inp):

    valleys_crossed = 0
    level = 0
    var = 0

    for char in inp:

        if char == 'U':
             if var == 'D':
                 valleys_crossed += 1

        var = char








    return valleys_crossed


print(counting_valleys(inp))
