def descending_order(num):
    descending = int("".join(sorted(str(num), reverse=True)))
    return descending


print(descending_order(42145))
print(descending_order(145263))
print(descending_order(123456789))
