inp = "Hello   World    OpenAI"

def reverse_words(s):

    words = s.split()

    reversed_words = words[::-1]

    reversed_string = ' '.join(reversed_words)

    return reversed_string

print(reverse_words(inp))