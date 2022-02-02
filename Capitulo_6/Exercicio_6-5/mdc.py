def mdc(a, b):
    if b == 0:
        return a
    else:
        r = a % b
        return mdc(b, r)


print(mdc(24, 36))
