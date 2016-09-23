#! /usr/bin/env python3


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for num in nums:
            ans ^= num
        return ans

    def old_singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h = {}
        for num in nums:
            if num in h:
                h.pop(num)
            else:
                h[num] = 1
        return list(h.keys())[0]


if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([1, 2, 3, 4, 4, 3, 1]))
