""" https://leetcode.com/problems/longest-substring-without-repeating-characters/ """

class Solution:
    def engthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        res = 0
        for i in range(length):
            for j in range(i, length):
                if self.is_unique(s[i:j + 1]):
                    res = max(res, j - i + 1)

        return res

    def is_unique(self, st):
        stlist = list(st)
        return list(set(stlist)) == stlist
