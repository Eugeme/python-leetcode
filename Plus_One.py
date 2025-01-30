# https://leetcode.com/problems/plus-one/description/

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        num = 0
        for d in digits:
            num = num * 10 + d

        num += 1

        if num == 0:
            return [0]

        digits = []
        while num > 0:
            digits.append(num % 10)
            num //= 10

        return digits[::-1]



instance = Solution()
res = instance.plusOne([1,2,3,9])
print(res)