# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = len(nums)
        for i in range(len(nums) - 1):
            while nums[i + 1] == nums[i] and nums[i] != -137:
                k -= 1
                nums.append(-137)
                nums.pop(i + 1)

        return k


instance = Solution()

res = instance.removeDuplicates([0,0,1,1,1,2,2,3,3,4])

print(res)
