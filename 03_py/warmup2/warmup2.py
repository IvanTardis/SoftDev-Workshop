Ivan Gontchar
Belugas
SoftDev
K03 -- Reviewing python lists
2024-09-12

def string_times(str, n):
  return str * n

def front_times(str, n):
  if len(str) < 3:
    return str*n
  return str[0:3]*n

def string_bits(str):
  return str[0:len(str):2]

def string_splosion(str):
  x = ""
  for i in range(len(str)):
    x += str[:i+1]
  return x

def last2(str):
  x = str[len(str)-2:]
  y=0
  for i in range(len(str) - 2):
    if(str[i:i+2] == x):
      y = y + 1
  return y

def array_count9(nums):
  return nums.count(9)

def array_front9(nums):
  if(len(nums) >= 4):
    for i in range(4):
      if nums[i] == 9:
        return True
  else:
    for i in range(len(nums)):
      if nums[i] == 9:
        return True
  return False

def array123(nums):
  for i in range(len(nums) - 2):
    if nums[i] == 1:
      if nums[i + 1] == 2:
        if nums[i + 2] == 3:
          return True
  return False

def string_match(a, b):
  total = 0
  max = ""
  min = ""
  if(len(a) > len(b)):
    max = a
    min = b
  else:
    max = b
    min = a
  for i in range(len(min) - 1):
    if max[i:i+2] == min[i:i+2]:
      total += 1
  return total
