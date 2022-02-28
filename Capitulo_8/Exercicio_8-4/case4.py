def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


word = 'bANANA'

print(any_lowercase4(word))

# Essa function estah CORRETA!
