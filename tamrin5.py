sentence = "I'm happy"
def swap_case(sentence):
    result = ''
    for char in sentence:
        if char.isupper():
            result += char.lower()
        elif char.islower():
            result += char.upper()
        else:
            result += char
    return result
print(swap_case(sentence))
        
            