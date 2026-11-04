"""def non_repeat(word):
    word = word.lower()

    for i in range(len(word)):
        is_unique = True

        for j in range(len(word)):
            if i != j and word[i] == word[j]:
                is_unique = False
                break

        if is_unique:
            return word[i]

    return None


word = input("Enter a word: ")
result = non_repeat(word)
print(result)
"""

def non_repeat(word):
    f ={}
    for i in word:
        f[i] = f.get(i,0) + 1
    for key in f.keys():
        if f[key] == 1:
            return key

    return None
print(non_repeat("aabccdeffggh"))
