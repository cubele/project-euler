# https://www.geeksforgeeks.org/program-to-find-lcm-of-two-numbers/
# https://www.geeksforgeeks.org/gcd-two-array-numbers/

def gcd(a, b):
    return b if a == 0 else gcd(b % a, a)

def lcm(a, b):
    return a * b // gcd(a, b)

def sumFirstNumbers(n):
    return n * (n + 1) // 2

lcm_num = 2520
for x in range(11, 21):
    lcm_num = lcm(lcm_num, x)

print(lcm_num)
