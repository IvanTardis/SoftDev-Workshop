# Ivan Gontchar
# Belugas
# SoftDev
# K03 -- Reviewing python 2.0
# 2024-09-11
# time spent: 2 minutes
def front_times(str, n):
  if len(str) < 3:
    return str*n
  return str[0:3]*n
