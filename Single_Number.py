# https://leetcode.com/problems/single-number/description/
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        for i in nums:
            if nums.count(i) == 1: return i


instance = Solution()
res = instance.singleNumber([4,1,2,1,2])
print(res)
