""" https://leetcode.com/problems/longest-substring-without-repeating-characters/ """

from collections import Counter


class Solution:
    def engthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        res = 0
        ch = Counter()
        lidx = ridx = 0

        while ridx < length:
            r = s[ridx]
            ch[r] += 1

            while ch[r] > 1:  # move window
                l = s[lidx]
                ch[l] -= 1
                lidx += 1
            res = max(res, ridx + 1 - lidx)
            ridx += 1

        return res
