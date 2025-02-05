# https://leetcode.com/problems/pascals-triangle/

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        diagonals = [[1] * numRows]
        for i in range(1, numRows):
            diagonals.append([sum(diagonals[-1][:x]) for x in range(numRows)])

        rows = [[elem[i] for elem in diagonals if elem[i] != 0] for i in range(numRows)]

        return rows


instance = Solution()
res = instance.generate(5)
print(res)
