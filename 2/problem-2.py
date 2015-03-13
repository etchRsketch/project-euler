#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def evenFibonacciNumbers(ourRange):
  x = 0
  y = 1
  sumOfEvens = 0
  while y < ourRange:
    if x % 2 == 0:
      sumOfEvens += x
    if y % 2 == 0:
      sumOfEvens += y
    print x
    print y
    x += y
    y += x
  print "sum of even numbers is " + str(sumOfEvens)

evenFibonacciNumbers(4000000)
    
