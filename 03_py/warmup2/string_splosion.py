# Ivan Gontchar
# Belugas
# SoftDev
# K03 -- Reviewing python 2.0
# 2024-09-11
# time spent: 2 minutes
def string_splosion(str):
  x = ""
  for i in range(len(str)):
    x += str[:i+1]
  return x
