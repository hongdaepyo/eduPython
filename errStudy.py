result = 0
try:
    [1, 2, 3][3]
    "a"+1
    4 / 0
except TypeError:
    result += 1
    print("TypeError")
except ZeroDivisionError:
    result += 2
    print("ZeroDivisionError")
except IndexError:
    result += 3
    print("IndexError")
finally:
    result += 4

print(result)