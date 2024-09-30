import typing

def count_smaller(nums: list):
  smaller_nums = []
  for i in range(len(nums)):
    count = 0
    for j in range(len(nums)):
      if i != j and nums[j] < nums[i]:
        count += 1
    smaller_nums.append(count)
  return smaller_nums

def main():
  nums = [8,1,2,2,3]
  print(count_smaller(nums)) # [4,0,1,1,3]

main()
