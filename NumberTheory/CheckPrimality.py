#This is a program to check the primality of a number. This is an extremely important and common in competitive programming
#Time complexity: O(root(n)) (maximum complexity)

from math import sqrt

def check_prime(n):
  if n == 0 or n==1:
    return False # not a prime
  if n ==2 or n ==3:
    return True # both 2 and 3 are primes
  if n%2 ==0 or n%3==0:
    return False
  else:
    for i in range(5, int(sqrt(n))+1):
      if n%i==0 or n%(i+2)==0:
          return False
     
  return True
