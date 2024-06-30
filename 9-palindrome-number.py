# problem :- Palindrome Number 

class Solution: 
    # step 1 : create a function which check input string 
    def is_palindrome(nums: int)-> bool:  
        # step 2 : Compare the input values 
        temp = str(nums)
        # print(temp)
        # print(type(temp))
        rev_temp = ''.join(reversed(temp))
        # print(rev_temp)
        # step 3 : Return the True or False
        if temp == rev_temp:
        print('true')
        else:
        print('false')

# Testing function and classname 
sol = Solution()
sol.is_palindrome(121)


