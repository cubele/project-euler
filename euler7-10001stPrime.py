import math

def primeNumberNth(n):
    logN = math.log(n)
    logLogN = math.log(logN)
    part1 = logN + logLogN - 1
    part2 = (logLogN - 2) / logN
    part3 = (logLogN * logLogN - 6 * logLogN + 11) / (2 * logN * logN)
    primeNth = n * (part1 + part2 - part3)
    return primeNth

print(primeNumberNth(6))