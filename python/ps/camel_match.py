''' https://leetcode.com/problems/camelcase-matching/ '''

from typing import List


class Solution:
    def camelMatch(self, queries: List[str], pat: str) -> List[bool]:
        result = []
        for que in queries:
            result.append(self.match(que, pat))

        return result

    def match(self, que, pat):
        i = 0
        for char in que:
            if i < len(pat) and pat[i] == char:
                i += 1
            elif char.isupper():
                return False

        return i == len(pat)  # scanned all pattern character



queries = ['FooBar','FooBarTest','FootBall','FrameBuffer','ForceFeedBack']
pattern = 'FoBa'
sol = Solution()
print(sol.camelMatch(queries, pattern))
