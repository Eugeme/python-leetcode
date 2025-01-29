# https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        s = s[::-1]

        if s[0] == ' ':
            first_letter = 0
            for i in range(len(s)):
                if s[i] == ' ':
                    first_letter += 1
                else:
                    break
            s = s[first_letter:]

        if len(s) == 1:
            return 1

        count = 0
        for i in range(len(s)):
            if s[i] != ' ':
                count += 1
            else:
                break

        return count


instance = Solution()
res = instance.lengthOfLastWord("Hello World")
res = instance.lengthOfLastWord("    Hello      World      ")
res = instance.lengthOfLastWord("World  ")
print(res)
