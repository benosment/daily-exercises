#! /usr/bin/env python3

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num
        else:
            n = num % 9
            if n == 0:
                return 9
            else:
                return n


if __name__ == '__main__':
    s = Solution()
    for i in range (0, 29):
        print(i, s.addDigits(i))
