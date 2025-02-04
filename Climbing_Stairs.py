# https://leetcode.com/problems/climbing-stairs/description/

class Solution:
    def climbStairs(self, n: int) -> int:

        def factorial(x):
            if x < 2:
                return 1
            else:
                return x * factorial(x - 1)

        result = 0 if n % 2 == 0 else 1

        if n % 2 != 0:
            count = 1
            for i in range((n//2)+1, n):
                permutations= int(factorial(i)/(factorial(i-count)*factorial(count)))
                result += permutations
                count += 2
        else:
            count = 0
            for i in range((n//2), n+1):
                permutations= int(factorial(i)/(factorial(i-count)*factorial(count)))
                result += permutations
                count += 2

        return result


instance = Solution()
res = instance.climbStairs(5)
print(res)
