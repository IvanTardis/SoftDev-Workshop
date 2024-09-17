# Ivan Gontchar
# Belugas
# SoftDev
# K03 -- Reviewing python 2.0
# 2024-09-11
# time spent: 2 minutes
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
