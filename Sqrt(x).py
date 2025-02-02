# https://leetcode.com/problems/sqrtx/description/

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0
        if x == 1: return 1

        for i in range(x+1):
            if i*i > x:
                return i-1

instance = Solution()
res = instance.mySqrt(122)
print(res)
