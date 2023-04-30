#import cryptographically safe random generator
from secrets import randbelow
from scipy.interpolate import lagrange
from math import floor
p = 1e9+7 # upper bound on the random numbers

# secret_int, store the message
# num_of_keys, number of keys we will generate
# min_keys, number of keys needed to decrypt
def threshold_enc(secret_int, num_of_keys, min_keys):
  """
  input: secret_int, num_of_keys, min_keys
  Generate a threshold encryption scheme
  return a dictionary of keys
  """
  poly = []
  poly.append(secret_int)
  for _ in range(min_keys-1):
    poly.append(randbelow(int(p)))

  #actual generation of n keys
  keys = {}
  for i in range(1, num_of_keys+1):
    # we have to find out Q(i)
    # poly array (i)
    ans = 0
    for exp, coef in enumerate(poly):
      ans += coef * int(pow(i, exp))
    keys[i] = ans
  return keys

def threshold_dec(keys):
  """
  input: keys
  return the secret int
  """
  x = []
  y = []
  for key in keys:
    x.append(key)
    y.append(keys[key])
  rounded = round(lagrange(x, y)(0))
  return rounded

if __name__ == "__main__":
  keys = threshold_enc(10, 5, 3)
  #keys= {1:1359604324, 2:3669531662, 3: 6929782024, 4: 11140355410, 5: 16301251820}
  print(keys)
  print(threshold_dec(keys))
