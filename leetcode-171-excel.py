class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = dict(zip(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), range(1, 27)))
        total = 0
        mult = 1
        for i in range(len(s)):
            val = s[len(s) - i - 1]
            total += mult * d[val]
            mult *= 26
        return total

if __name__ == '__main__':
    s = Solution()
    print(s.titleToNumber('Z'))
    print(s.titleToNumber('AA'))
    print(s.titleToNumber('AB'))
    print(s.titleToNumber('BA'))
