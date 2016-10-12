#! /usr/bin/env python3

class Solution(object):
    def hex_string(self, num):
        if num < 10:
            return str(num)
        elif num == 10:
            return 'a'
        elif num == 11:
            return 'b'
        elif num == 12:
            return 'c'
        elif num == 13:
            return 'd'
        elif num == 14:
            return 'e'
        elif num == 15:
            return 'f'
        else:
            return 'ERROR'

    def toHex(self, num):
        ans = ''
        if num < 0:
            num = 2 ** 32 + num
        if num == 0:
            return '0'
        while num:
            div = int(num / 16)
            if div > 0:
                rem = num - div * 16
            else:
                rem = num
            ans = self.hex_string(rem) + ans
            num = div

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.toHex(-1))
