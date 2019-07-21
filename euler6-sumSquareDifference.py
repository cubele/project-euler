def sumFirstNumbers(n):
    return n * (n + 1) // 2

def sumFirstSquaredNumbers(n):
    return n * (n + 1) * (2*n + 1) // 6

N = 100
s = sumFirstNumbers(N)
sum_square = s * s
square_sum = sumFirstSquaredNumbers(N)

print(sum_square - square_sum)
