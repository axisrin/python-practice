import math

def __task1__(x,y):
    exponent = 0
    answer = (((x**7)-math.sin(y))**5 + math.sin(x) + (((13*((y)**4))-x**6)/((92*(x**3))+math.tan(y))) + y**6 + math.exp(1)**y)
    # if (answer > 0):
    #     while (answer % 10 == 0):
    #         exponent += 1
    #         answer %= 10
    return answer

print("f(36,-52) = {:e}".format(__task1__(36,-52)))
print("f(-31,29) = {:e}".format(__task1__(-31,29)))

def __task2__ (x):
    if x < -66:
        answer = x**7 + x**5 + 53
    if -66 <= x < -36:
        answer = 72*x**7 - math.exp(1)**x + 20
    if -36 <= x < 63:
        answer = x**5 - x**7
    if 63 <= x < 97:
        answer = x**5 + x**7
    if 97 <= x:
        answer = 76*x - ((x**8)/74)

    return answer

print("f(-71) = {:e}".format(__task2__(-71)))
print("f(36) = {:e}".format(__task2__(36)))

def __task3__ (x):
    firstNumeralRow = 0
    firstRange = 1
    for firstRange in range(x+1):
        firstNumeralRow += ((92)*(firstRange**3)+(math.tan(firstRange)))
    secondNumeralRow = 0
    secondRange = 1
    for secondRange in range(x+1):
        secondNumeralRow += ((92)*(secondRange**4)+(secondRange**7))
    answer = 38*firstNumeralRow - secondNumeralRow

    return answer

print("f(89) = {:e}".format(__task3__(89)))
print("f(62) = {:e}".format(__task3__(62)))

def __task4__ (x):
    if x == 0:
        return 8

    answer = ((math.tan(__task4__(x-1))) - (1/64)*((__task4__(x-1))**2))
    return answer

print("f(2) = {:e}".format(__task4__(2)))
print("f(5) = {:e}".format(__task4__(5)))