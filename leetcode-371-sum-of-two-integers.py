class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MAX_INT = 0xFFFFFFFF
        MAX_POS = 0x80000000
        while b != 0:
            a = a & MAX_INT
            b = b & MAX_INT
            a, b = a ^ b, (a & b) << 1
        if a > MAX_POS:
            return - ((a ^ MAX_INT) + 1)
        else:
            return a


if __name__ == '__main__':
    s = Solution()
    print(s.getSum(1, 2))
    print(s.getSum(4, 3))
    print(s.getSum(20, 30))
    print(s.getSum(-2, 1))
    print(s.getSum(-1, 1))
