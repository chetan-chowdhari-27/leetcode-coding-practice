class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Remove non-alphanumeric characters and convert to lowercase
        s = ''.join(char.lower() for char in s if char.isalnum())
        # Check if the string is equal to its reverse
        return s == s[::-1]
