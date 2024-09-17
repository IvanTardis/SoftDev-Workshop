# Ivan Gontchar
# Belugas
# SoftDev
# K03 -- Reviewing python 2.0
# 2024-09-11
# time spent: 2 minutes
def array123(nums):
  for i in range(len(nums) - 2):
    if nums[i] == 1:
      if nums[i + 1] == 2:
        if nums[i + 2] == 3:
          return True
  return False
