# Single Number
# Input: nums = [2,2,1]  Output: 1
# Input: nums = [4,1,2,1,2]  Output: 4

from collections import Counter

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        counter = Counter(nums)
        duplicates = [item for item, count in counter.items() if count <= 1]
        new_list = duplicates[0]
        return new_list

sol= Solution()
print(sol.singleNumber([4,1,2,1,2]))


# without libraries 

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        counters = {}
        for num in nums:
          if num in counters:
            counters[num] +=1
          else:
            counters[num] =1

        duplicates = [item for item, count in counters.items() if count <= 1]
        new_list = duplicates[0]
        return new_list

sol= Solution()
print(sol.singleNumber([9,1,2,1,2,8,8]))
