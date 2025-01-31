# https://leetcode.com/problems/add-binary/description/

class Solution:
    def addBinary(self, a: str, b: str) -> str:

        if len(a) < len(b):
            a = '0' * abs(len(b) - len(a)) + a
        else:
            b = '0' * abs(len(a) - len(b)) + b
        a = a[::-1]
        b = b[::-1]
        c = ''
        add = 0
        for i in range(len(a)):
            sum = int(a[i]) + int(b[i]) + add
            if sum == 0:
                c += '0'
                add = 0
            elif sum == 1:
                c += '1'
                add = 0
            elif sum == 2:
                c += '0'
                add = 1
            elif sum == 3:
                c += '1'
                add = 1

        if add == 1:
            c += '1'

        c = c[::-1]
        return c


instance = Solution()
res = instance.addBinary("100", "110010")
print(res)
