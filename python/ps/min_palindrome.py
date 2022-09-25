''' https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/ '''


class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        s = list(s)
        length = len(s)

        count = 0

        for left in range(length // 2):
            right = length - left - 1
            if s[left] != s[right]:
                i = left
                j = right

                while s[left] != s[j]:
                    j -= 1

                while s[right] != s[i]:
                    i += 1

                if right - j < i - left:
                    count += right - j
                    for x in range(j, right):
                        s[x] = s[x + 1]
                else:
                    count += i - left
                    for x in range(i, left, -1):
                        s[x] = s[x - 1]
        return count
