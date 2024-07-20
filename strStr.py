class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # checking if need is empty then 0 
        if not needle:
            return 0  # return it 

        # checking the lenght of needle greater then haystack
        if len(needle) > len(haystack):
            return -1
        
        # iterating the haystack 
        for i in range(len(haystack) - len(needle) + 1):
            # Extract the substring from haystack 
            if haystack[i:i + len(needle)] == needle:
                return i 
            
        return -1 

        


sol = Solution()
print(sol.strStr("leetcode",'leetco'))