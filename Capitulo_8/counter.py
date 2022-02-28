def count(word, letter):
    count = 0
    for car in word:
        if car == letter:
            count += 1
    return count


print(count('banana', 'a'))
