import string
def is_pangram(s):
    lowercase_sentence = s.lower()

    alphabet = list(string.ascii_lowercase)
    characters = []
    for char in lowercase_sentence:
        if char.isalpha():  # Check if the character is an alphabet letter
            characters.append(char)
    count = 0

    set_characters = list(set(characters))
    for i in range(len(set_characters)):
        for j in range(len(alphabet)):
            if len(set_characters) == len(alphabet):
                return True
            return False
result = is_pangram("The quick brown fox jumps over the lazy dog")
print(result)