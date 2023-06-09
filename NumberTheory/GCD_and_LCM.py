#GCD and LCM of two numbers can be found using Euclid's algorith in time complexity of O(log(min(a,b))).
# Theorem: product = LCM*GCD

def GCD(a, b):
  if a == b:
    return b
  return GCD(b%a, a)
def lcm(a,b):
  product = a*b
  hcf = GCD(a, b)
  return product//hcf
  
a, b = map(int, input().split())
print(GCD(a,b))
print(lcm(a,b))
