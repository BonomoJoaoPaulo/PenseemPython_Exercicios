
def check_fermat(a, b, c, n):
    if a**2 + b**2 == c**n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")


A, B, C, N = [int(x) for x in input("Digite respectivamente os valores a, b, c, n:\n").split()]

check_fermat(A, B, C, N)
