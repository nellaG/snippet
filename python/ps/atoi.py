""" https://leetcode.com/problems/string-to-integer-atoi/ """


class Solution:
    def myAtoi(self, s: str) -> int:
        ls = list(s.strip())
        if len(ls) == 0:
            return 0

        sign = -1 if ls[0] == "-" else 1

        if ls[0] in ["-", "+"]:
            del ls[0]

        i = 0
        ret = "0"

        while i < len(ls) and ls[i].isdigit():
            print(ret)
            ret += ls[i]
            i += 1
        answer = int(ret)
        return max(-(2**31), min(sign * answer, 2**31 - 1))


sol = Solution()

st = "000000-12a12343"  # 0

print(sol.myAtoi(st))
