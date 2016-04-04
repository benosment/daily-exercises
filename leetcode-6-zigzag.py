#! /usr/bin/env python3

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        ans = ''
        for i in range(numRows):
            ans += ''.join([s[c] for c in range(i, len(s), numRows + 1)])
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.convert('PAYPALISHIRING', 3))
