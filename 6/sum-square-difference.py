#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sumOfSquares (number):
  number += 1
  ourSum = 0
  for x in range(0, number):
    ourSum += x * x
  return ourSum

def squareOfSums (number):
  number += 1
  sums = sum(range(0, number))
  return sums * sums

def sumSquareDifference(number):
  return squareOfSums(number) - sumOfSquares(number)

print sumSquareDifference(100)
