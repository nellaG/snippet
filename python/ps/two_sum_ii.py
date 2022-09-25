""" https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/ """

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        hmap = {}
        length = len(numbers)
        for i in range(length):
            hmap[numbers[i]] = i

        for i in range(length):
            subt = target - numbers[i]
            if subt in hmap and hmap[subt] != i:
                return [i + 1, hmap[subt] + 1]

        return []
