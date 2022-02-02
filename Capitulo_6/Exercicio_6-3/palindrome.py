def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]


def is_palindrome(word):
    if len(word) <= 1:
        return "Palavras com 1 letra nao podem ser palíndromos"
    elif len(word) >= 3:
        return first(word) == last(word) and middle(word) == middle(word[::-1])
    else:
        return first(word) == last(word)
            

palavra = "rever"

print(is_palindrome(palavra))
