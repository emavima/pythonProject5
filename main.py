def is_anagram(w1, w2):

    res1 = ''.join(sorted(w1)).lower().strip()
    res2 = ''.join(sorted(w2)).lower().strip()

    return res1 == res2


print(is_anagram("listen", "silent"))
print(is_anagram("Anagram", "nag a ram"))
print(is_anagram("Hello", "World"))


