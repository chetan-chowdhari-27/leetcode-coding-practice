class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:

        counters = {}
        for num in nums:
            if num in counters:
                counters[num] += 1
            else:
                counters[num] = 1

        return any(count > 1 for count in counters.values())

        # return 


sol = Solution()
print(sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))