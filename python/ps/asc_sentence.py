""" https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/ """


class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        holder = ""
        s += "X"  # do not allow when last string is digit
        last = 0
        for st in s:
            if st.isdigit():
                holder += st
            else:  # letter or space
                if holder != "":
                    if last >= int(holder):
                        return False
                    last = int(holder)
                    holder = ""

        return True


sol = Solution()
st = [
    "1 box has 3 blue 4 red 6 green and 12 yellow marbles",
    "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s",
    "hello world 5 x 5",
]
for s in st:
    print(sol.areNumbersAscending(s))
