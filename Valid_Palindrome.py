# https://leetcode.com/problems/valid-palindrome/description/
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^a-zA-Z0-9]', '', s)

        return s == s[::-1]



instance = Solution()
res = instance.isPalindrome("race a car")
print(res)
