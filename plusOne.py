class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        merge_dig =int("".join(map(str, digits))) + 1
        merge_fi = []
        for i in str(merge_dig):
            merge_fi.append(int(i))
        return  merge_fi
    
sol = Solution()
print(sol.plusOne([1,2,3]))