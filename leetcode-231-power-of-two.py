#!/usr/bin/env python3


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        if n & n - 1 == 0:
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfTwo(1))
    print(s.isPowerOfTwo(2))
    print(s.isPowerOfTwo(100))
    print(s.isPowerOfTwo(128))
