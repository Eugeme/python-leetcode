# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = None
        max = None
        max_prof = 0
        for price in prices:
            if min is None or price < min:
                min = price
                max = price
            if price > max:
                max = price
            if max - min > max_prof:
                max_prof = max - min

        return max_prof


instance = Solution()
res = instance.maxProfit([7,6,4,3,1])
print(res)