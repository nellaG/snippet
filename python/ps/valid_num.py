""" https://leetcode.com/problems/valid-number/ """


class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        s = s.replace('E', 'e')
        dot = e = digit = False

        for i, st in enumerate(s):
            if st in ['+', '-']:
                if i > 0 and s[i - 1] != 'e':  # 3e-1, 3e+3
                    return False
            elif st == '.':  # e should be after to .
                if dot or e:
                    return False
                dot = True
            elif st == 'e':  # e should be after to digit (and only can be)
                if e or not digit:
                    return False
                e = True
                digit = False
            elif st.isdigit():
                digit = True
            else:
                return False
        return digit


sol = Solution()
valid = [
    '2',
    '0089',
    '-0.1',
    '+3.14',
    '4.',
    '-.9',
    '2e10',
    '-90E3',
    '3e+7',
    '+6e-1',
    '53.5e93',
    '-123.456e789',
]

for v in valid:
    print(f'{v}, {sol.isNumber(v)}')

invalid = ['abc', '1a', '1e', 'e3', '99e2.5', '--6', '-+3', '95a54e53']
for inv in invalid:
    print(f'{inv}, {sol.isNumber(inv)}')
