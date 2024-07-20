# 43. Multiply Strings
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = int(num1)
        num2 = int(num2)

        multiply = num1 * num2
        return str(multiply)

sol = Solution()
print(sol.multiply("123", "456"))