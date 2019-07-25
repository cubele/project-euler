import math

def isPrime(num):
  for x in range(2, int(math.sqrt(num)) + 1):
    if num % x == 0:
      return False
  return True

N = 2000000
sum = 0
for num in range(2, N):
  if isPrime(num):
    sum += num

print(sum)
