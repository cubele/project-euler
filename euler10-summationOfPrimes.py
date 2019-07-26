# import math

# def isPrime(num):
#   for x in range(2, int(math.sqrt(num)) + 1):
#     if num % x == 0:
#       return False
#   return True

# N = 2000000
# sum = 0
# for num in range(2, N):
#   if isPrime(num):
#     sum += num

# print(sum)


class Primes:
  def __init__(self, threshold):
    self.output = ''

    self.threshold = threshold
    self.primes = list(range(2, threshold))
    self.primesLen = len(self.primes)

    self.crossed = [False] * self.primesLen

    self.lastPrimeIndex = 0

    self.cross()
    while True:
      nextIndex = self.nextPrimeIndex()
      if not nextIndex:
        return
      self.cross

  def cross(self):
    prime = self.primes[self.lastPrimeIndex]
    index = self.lastPrimeIndex + prime
    while(index < self.primesLen):
      self.crossed[index] = True
      index += prime

  def nextPrimeIndex(self):
    index = self.lastPrimeIndex
    while(True):
      index += 1
      if index >= self.primesLen:
        return None
      if not self.crossed[index]:
        index
    self.lastPrimeIndex = index
    
  def __str__(self):
    return self.output

  def display(self):
    for index in range(self.primesLen):
      if self.crossed[index]:
        print('x' + str(self.primes[index]), end=', ')
      else:
        print(str(self.primes[index]), end=', ')
    

euler10 = Primes(100)
euler10.display()
