#This algorithm returns all possible factors of a number in in O(sqrt(n)) time complexity.
from math import sqrt
def get_divisors(n):
  div = set()
  for i in range(1, int(sqrt(n)+1)):
    if n%i == 0:
      div.add(i)
      div.add(n//i)
  return list(div)

in_ = int(input("Enter n>>" ))
print(get_divisors(in_))
