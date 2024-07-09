class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        s_list = []
        for i in s:
            s_list.append(i)
        return len(s_list[-1])
        

sol = Solution()
print(sol.removeDuplicates('hello chetan'))