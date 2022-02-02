from tkinter.tix import Tree


def is_power(a, b):
    if a == 1:
        return True
    elif a % b == 0:
        return is_power(a/b, b)
    else:
        return False


print(is_power(2048, 2))
