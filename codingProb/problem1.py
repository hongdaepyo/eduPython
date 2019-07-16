# multiples of 3 and 5 // https://projecteuler.net/problem=1

def getSum():
    sum = 0
    for x in range(1000):
        if x % 3 == 0 or x % 5 == 0:
            sum += x
    return sum

getSum()