def duplicate_encode(word):
    #your code here
    lowercase_word = word.lower()
    chars = {}

    for char in lowercase_word:
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1

    new_string = ""
    for char in lowercase_word:
        if chars[char] == 1:
            new_string += "("
        else:
            new_string += ")"
    return new_string
