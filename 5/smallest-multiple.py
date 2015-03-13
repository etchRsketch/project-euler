#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def divisibleByRange(number, ourRange):
  ourRange += 1
  for x in range(1, ourRange):
    if number % x != 0:
      return False
  return True

def smallestMultiple(ourRange):
  divisible = False
  x = 2520
  while divisible == False:
    x += 2520
    divisible = divisibleByRange(x, ourRange)
  return x


print "the smallest multiple is " + str(smallestMultiple(20))
  
