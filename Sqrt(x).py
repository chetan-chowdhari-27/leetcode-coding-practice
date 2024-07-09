import numpy as np
class Solution:
    def mySqrt(self, x: int) -> int:
        new_num = int(np.sqrt(x))
        return new_num
    
sol = Solution()
sol.mySqrt(4)