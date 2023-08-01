
def word_length_counter(sen):

    s3 = sen.replace(',', '')
    s2 = s3.replace('!', '')
    s1 = s2.replace('.', '')
    s = s1.replace('?', '')

    lst_s = s.split()


    dict = {}

    for i, char in enumerate(lst_s):

        dict[char] = len(lst_s[i])


    return dict



print(word_length_counter("Hello, world!"))