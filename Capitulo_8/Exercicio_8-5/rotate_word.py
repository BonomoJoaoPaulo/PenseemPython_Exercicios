def rotate_word(word, rot):
    new_word = ''
    for c in word.lower():
        new_word += chr(ord(c) + rot)

    return new_word.title()


print(rotate_word('Banana', 1))
