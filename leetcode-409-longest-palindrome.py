#! /usr/bin/env python3

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {}
        for letter in s:
            count[letter] = count.get(letter, 0) + 1
        at_least_one_odd = False
        total_even = 0
        for (letter, count) in count.items():
            if count % 2 == 1:
                at_least_one_odd = True
                count -= 1
            total_even += count
        if at_least_one_odd:
            return total_even + 1
        else:
            return total_even


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome('abccccdd'))
