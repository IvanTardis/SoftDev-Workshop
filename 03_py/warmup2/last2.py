# Ivan Gontchar
# Belugas
# SoftDev
# K03 -- Reviewing python 2.0
# 2024-09-11
# time spent: 2 minutes
def last2(str):
  x = str[len(str)-2:]
  y=0
  for i in range(len(str) - 2):
    if(str[i:i+2] == x):
      y = y + 1
  return y
