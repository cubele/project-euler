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


def sumPrimes(n):
  primes = list(range(2, n))
  crossed = [False] * len(primes)
  i = -1
  while True:
    currentPrimeIndex = i + 1
    while crossed[currentPrimeIndex]:
      currentPrimeIndex += 1
    
    print(currentPrimeIndex)
    currentPrime = primes[currentPrimeIndex]

    nextIndex = currentPrimeIndex
    for p in range(1, n // currentPrime - 1):
      nextIndex += currentPrime
      crossed[nextIndex] = True
      print(crossed)

  
    if i > len(primes):
      break

    i = currentPrimeIndex + 1

sumPrimes(10)
