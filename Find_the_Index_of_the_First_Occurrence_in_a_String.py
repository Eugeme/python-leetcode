# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        occurrences = []
        for x in range(len(haystack)):
            if needle == haystack[x:len(needle)+x]:
                occurrences.append(x)
        if occurrences:
            return occurrences[0]
        else:
            return -1


instance = Solution()
haystack = "leetcode"
needle = "leeto"
result = instance.strStr(haystack, needle)

print(result)