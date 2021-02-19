def __twenty_multiple_with_pluses__(x):
    x = x+x+x
    x = x + x
    x = x + x
    return x
print()
print("Умножение на 12. Сложением 4 раза.")
print("f({0}) = {1}".format(1,__twenty_multiple_with_pluses__(1)))
print("f({0}) = {1}".format(2,__twenty_multiple_with_pluses__(2)))
print("f({0}) = {1}".format(3,__twenty_multiple_with_pluses__(3)))
print("f({0}) = {1}".format(6,__twenty_multiple_with_pluses__(6)))

def __sixteen_multiple_with_pluses__(x):
    x =  x+x
    x = x + x
    x =  x+x
    x = x + x
    return x
print()
print("Умножение на 16. Сложением 4 раза.")
print("f({0}) = {1}".format(1,__sixteen_multiple_with_pluses__(1)))
print("f({0}) = {1}".format(2,__sixteen_multiple_with_pluses__(2)))
print("f({0}) = {1}".format(3,__sixteen_multiple_with_pluses__(3)))
print("f({0}) = {1}".format(6,__sixteen_multiple_with_pluses__(6)))

def __fifteen_multiple_with_pluses__(x):
    a = x + x
    a = a + a
    a = a + a
    a = a + a
    x = a - x
    return x
print()
print("Умножение на 15. Сложением 4 раза и минусованием 1 раз.")
print("f({0}) = {1}".format(1,__fifteen_multiple_with_pluses__(1)))
print("f({0}) = {1}".format(2,__fifteen_multiple_with_pluses__(2)))
print("f({0}) = {1}".format(3,__fifteen_multiple_with_pluses__(3)))
print("f({0}) = {1}".format(6,__fifteen_multiple_with_pluses__(6)))


def __twentynine_multiple_with_pluses__(x):
    a = x + x
    a = a + a
    a = a + x
    a = a+a+a
    x = a+a-x
    return x
print()
print("Умножение на 29. Сложением 6 раз и 1 вычитанием.")
print("f({0}) = {1}".format(1,__twentynine_multiple_with_pluses__(1)))
print("f({0}) = {1}".format(2,__twentynine_multiple_with_pluses__(2)))
print("f({0}) = {1}".format(3,__twentynine_multiple_with_pluses__(3)))
print("f({0}) = {1}".format(6,__twentynine_multiple_with_pluses__(6)))