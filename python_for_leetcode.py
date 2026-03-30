n = 10
output = ''

while n >= 0:
  output += f' {n}'
  n -= 1

for i in range(-1, -11, -1):
  output += f' {i}'

print(output)

import math

print(10 / 3, # decimal division
      10 // 3, # rounds down int
      -10 // 3, # rounds down (not to 0)
      int(-10 / 3), # rounds int to 0
      10 % 3, 
      -10 % 3, # -10 + 3x4 = -2 (weird)
      math.fmod(-11, 3), # -2.0 (float)
      3+4,
      3*4, # int
      8/4 # float
      )

print(math.floor(3/2) < float('inf'),
      math.ceil(3/2) > float('-inf'),
      math.sqrt(9),
      math.pow(3, 2)
      )

arr = [1, 2] * 3
arr = [i for i in range(5)]
arr.pop(1) # can use index
arr.append(11)
arr.insert(0, 22)

print(arr, len(arr), arr[1::2])

# number of elements must match
a, b, c = [1, 2, 3]
print(a, b, c)

for index, element in enumerate(arr):
  print(index, element)

odds = [i for i in range(1, 10, 2)]
evens = [i for i in range(0, 10, 2)]

for x, y in zip(odds, evens):
  print(x, y)

zipped = list(zip(odds, evens))
zipped.reverse()
print(zipped)
zipped.sort() # reverse=True 
print(zipped)

words = ['hello', 'world', 'the', 'python', 'to']
words.sort(key = lambda x: len(x))
print(words)