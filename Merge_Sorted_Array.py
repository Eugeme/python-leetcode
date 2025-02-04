# https://leetcode.com/problems/merge-sorted-array/description/
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums2 = [0] * m + nums2

        for i in range(m, len(nums1)):
            nums1[i] = nums2[i]
        nums1.sort()


instance = Solution()
instance.merge([1,2,3,0,0,0], 3, [2,5,6], 3)
