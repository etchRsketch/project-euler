#Find the largest palindrome made from the product of two 3-digit numbers

#largest product of two 3-digit numbers is 999^2 = 998001

def isPalindrome(number):
  string = str(abs(number))
  digits = len(string)
  firstHalf = string[: digits/2]
  if digits % 2 == 0:
    secondHalf = string[digits/2: ]
  else:
    secondHalf = string[(digits/2) + 1: ]
  if firstHalf == secondHalf[::-1]:
    return True
  else:
    return False

def findLargestPalindrome():
  palindromes = []
  for x in range(1000, 0, -1):
    for y in range(x, 0, -1):
      if isPalindrome(x * y):
        palindromes.append(x * y)
  return max(palindromes)

print findLargestPalindrome()
