class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        num_ones = 0
        while n:
            if n & 1:
                num_ones += 1
            n = n >> 1
        return num_ones


if __name__ == '__main__':
    s = Solution()
    print(s.hammingWeight(15))
