def solution(s):
    result = ''
    for word in s:
        if word.isupper():
            result += ' ' + word
        else:
            result += word
    return result


