class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0 # inistiailzinf null 
        for j in range(1, len(nums)):
            if nums[i] != nums[j]: # comparing I and J 
                i += 1 # increment ++1 
                nums[i] = nums[j] # checking the duplicates 
        return i + 1 # Final output to + 1 

 

sol = Solution()
print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))