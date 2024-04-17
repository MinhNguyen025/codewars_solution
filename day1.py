def spin_words(sentence):
    words = sentence.split(" ")
    for i in range(len(words)):
        if len(words[i]) >= 5:
            words[i] = words[i][::-1]
    return " ".join(words)

if __name__ == "__main__":
    print(spin_words("Hey fellow warriors"))  # "Hey wollef sroirraw"
    print(spin_words("This is a test"))        # "This is a test"
    print(spin_words("This is another test"))  # "This is rehtona test"