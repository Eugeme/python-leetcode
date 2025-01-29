# https://leetcode.com/problems/search-insert-position/
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[-1] < target:
            return len(nums)

        i = 0
        for i in range(len(nums)):
            if nums[i] >= target:
                return i

instance = Solution()
res = instance.searchInsert([1,3,5,6], 5)
print(res)
