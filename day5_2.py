def to_camel_case(text):
    parts = text.replace("-","_").split("_")
    camel_case = parts[0] + "".join(word.capitalize() for word in parts[1:])
    return camel_case