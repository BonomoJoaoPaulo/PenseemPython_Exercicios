from unittest import result


def is_palindrome(word):
    new_word = word.upper()
    if new_word == new_word[::-1]:
        result = 'Is palindrome!'
    else:
        result = 'Is not palindrome!'
    return result

    
print(is_palindrome('Rever'))
