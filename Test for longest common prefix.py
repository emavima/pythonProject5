from longest_common_prefix import longest_common_prefix_1, longest_common_prefix_2

def test_longest_common_prefix(longest_common_prefix_2):

    inp_1 = []
    inp_2 = ['word']
    inp_3 = ['word', 'world', 'work', 'worm', 'wok']
    inp_4 = ['clock', 'pen', 'jacuzzi', 'shit', 'lip']
    inp_5 = ['ffaggot', 'ffanny', 'ffallout', 'ffamily']
    inp_6 = ['shit', 'shit', 'shit', 'shit', 'shit', 'shit', 'shit', 'shit', 'cacat']

    result1 = longest_common_prefix_2(inp_1)
    result2 = longest_common_prefix_2(inp_2)
    result3 = longest_common_prefix_2(inp_3)
    result4 = longest_common_prefix_2(inp_4)
    result5 = longest_common_prefix_2(inp_5)
    result6 = longest_common_prefix_2(inp_6)

    return result1, result2, result3, result4, result5, result6


print(test_longest_common_prefix(longest_common_prefix_2))