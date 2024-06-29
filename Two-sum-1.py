class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        num_dict = {}

        for i, num in enumerate(nums):
            complement = target - num 
            print(complement)

            if complement in num_dict:
               return  [num_dict[complement],i]
            
            num_dict[num] = i

        return []


    
# Test the function
sol = Solution()
print(sol.twoSum([1, 2, 3, 4,5], 9))



