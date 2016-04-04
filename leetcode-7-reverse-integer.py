#! /usr/bin/env python3

class Solution(object):
    def reverse(self, x):
        s = str(x)
        swap = None
        if s[0] == '-':
            swap = s[1:]
            swap = swap[::-1]
            ans =  int(s[0] + swap)
        else:
            swap = s[::-1]
            ans = int(swap)
        if abs(ans) > pow(2,32):
            return 0
        else:
            return ans



if __name__ == '__main__':
    s = Solution()
    print(s.reverse(123))
    print(s.reverse(-123))
