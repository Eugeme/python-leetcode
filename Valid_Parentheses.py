# https://leetcode.com/problems/valid-parentheses/description/


class Solution:
    def isValid(self, s: str) -> bool:

        if ((len(s) % 2 != 0) or s[0] in ')}]' or s[-1] in '({['): return False

        for _ in range(len(s) // 2):
            s = s.replace('{}', '').replace('[]', '').replace('()', '')

        return len(s) == 0
instance = Solution()

is_valid = instance.isValid("({[][()()]{[]}{(})})")

print(is_valid)
