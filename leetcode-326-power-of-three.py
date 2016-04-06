#!/usr/bin/env python3

import math

class Solution(object):
    # def isPowerOfThree(self, n):
    #     """
    #     :type n: int
    #     :rtype: bool
    #     """
    #     if n <= 0:
    #         return False
    #     val = int(round((math.log(n, 3)))
    #     if int(math.pow(3, val)) == n:
    #         return True
    #     return False

# class Solution(object):
#     def __init__(self):
#         self.powers = [math.pow(3, n) for n in range(0,21)]

#     def isPowerOfThree(self, n):
#         """
#         :type n: int
#         :rtype: bool
#         """
#         return n in self.powers


    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while True:
            n = n / 3.0
            if n == 1.0:
                return True
            if n < 1.0:
                return False

if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfThree(1))
    print(s.isPowerOfThree(3))
    print(s.isPowerOfThree(9))
    print(s.isPowerOfThree(100))
    print(s.isPowerOfThree(128))
    print(s.isPowerOfThree(36))
