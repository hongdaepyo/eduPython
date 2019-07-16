# Even Fibonacci numbers // https://projecteuler.net/problem=2

def fibo():
    n1 = 1
    n2 = 2
    tmp = 0
    idx = 2
    sum = 0
    nEnd = 4 * 10**6
    while n2 < nEnd:
        tmp = n1 + n2
        if n2 % 2 == 0:
            sum += n2
        n1 = n2
        n2 = tmp
        idx += 1
    return sum


fibo()