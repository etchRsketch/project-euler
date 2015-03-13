#What is the largest prime factor of the number 600851475143 ?
import math

def largestPrimeFactor(number):
  divisor = isComposite(number)
  if divisor:
    quotient = number / divisor
    print str(number) + "/ " + str(divisor) + " = " + str(quotient)
    largestPrimeFactor(quotient)
  else:
    print str(number) + " is prime"
    return number

def isComposite (number):
  for x in range(2, int(math.sqrt(number) + 1)):
    if number % x == 0:
      return x
  return False

q = 600851475143
print ""
print largestPrimeFactor(q)
