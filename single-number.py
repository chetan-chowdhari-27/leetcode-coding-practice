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