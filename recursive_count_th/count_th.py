'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # keep tracking of th number in the word
    th = 0
    # check base : terminates the process
    if len(word) <= 1:
        return th
    else:
        # check the length of the word
        if len(word) >= 2:
            # if we do have the "th" in the word
            if word[:2] == "th":
                th = 1
            return th + count_th(word[1:])
    return th


print(count_th(" "))  # 0
print(count_th("th"))  # 1
print(count_th("thth"))  # 2
