''' https://leetcode.com/problems/percentage-of-letter-in-string/ '''


class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        length = len(s)
        count = 0

        for st in s:
            if letter == st:
                count += 1

        return int(count / length * 100)
