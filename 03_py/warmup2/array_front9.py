# Ivan Gontchar
# Belugas
# SoftDev
# K03 -- Reviewing python 2.0
# 2024-09-11
# time spent: 2 minutes
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
