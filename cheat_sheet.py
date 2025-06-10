# Multiple Assignments
x, y = 10, 20
x, y = 22, 11
print(x, y)
x, y = [1, 2] # unpacking

# None is null (absence of value)
z = None

# If statements don't need parentheses unless multi-line
# and instead of &&, or instead of ||
if (z == None and
    True):
  print("This prints")

# Loops
n = 0
while n < 5:
  n += 1

for i in range(2, 0, -1):
  print(i)

# iterate through both index and values
for i, num in enumerate(['a', 'b', 'c']):
  print(i, num)

# iterate through multiple arrays
for x, y in zip([1, 2, 3], [9, 8, 7]):
  print(x, y)

# Math quirks to watch out for
print(-3 // 2) # floor division rounds down to -2
print(-10 % 3) # = 2, weird quirk with python

# Max / Min Int
float("inf")
float("-inf")

# Lists
arr = [1] * 3 # initialize list with default values
arr.append(4)
arr.pop()
arr.insert(1, 5)
print(arr, len(arr), arr[1:3])
arr.sort(reverse=True) # sort or reverse sort in place
arr.reverse() # just reverse in place
print(arr)
arr = ["bob", "alice", "jane", "doe"]
arr.sort(key=lambda x: len(x))
print(arr)
arr = [i*2 for i in range(5)] # List comprehension
print(arr)
arr = [[i] * 4 for i in range(4)] # 2-D list comprehension
print (arr) # arr = [[0] * 4] * 4 won't work