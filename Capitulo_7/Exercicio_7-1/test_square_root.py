from cgi import test
from re import X
import sys
import math

def mysqrt(a, x = 3):
    while True:
        y = (x + a/x) / 2
        if abs(y-x) < sys.float_info.epsilon:
            return y
        x = y


def test_square_root(a, mysqrt):
    raiz = math.sqrt(a)
    diff = abs(mysqrt-raiz)
    return f"{a}      {mysqrt}       {raiz}       {diff}"


print("a  mysqrt(a)  math.sqrt(a)  diff\n"
          "-  ---------  ------------  ----")

for num in range(1, 11):
    print(test_square_root(num, mysqrt(num)))
