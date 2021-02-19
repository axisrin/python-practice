import math

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

# 88 = '88' SyntaxError: cannot assign to literal

# name = weqwe SyntaxError: invalid syntax

# def __giro_giro__(): NameError: name 'a' is not defined
#     a = "FROGIE"
# print(a)

# x=input() При Вводе уйуйцуцйу програма выдаст TypeError: unsupported operand type(s) for -: 'str' and 'int'
# ans=x-10

# def win(): IndentationError: expected an indented block
# weqe = 1

# 0/0 ZeroDivisionError: division by zero

# math.asin(1231320) ValueError: math domain error

# math.exp(-4*10023123123123123123120000*-0.0641515994131312312321312312312321312312308) OverflowError: math range error