class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache = {}
        if n == 0:
            return 0
        return self.steps_helper(n, cache)

    def steps_helper(self, n, cache):
        if n < 0:
            return 0
        if n == 1 or n == 0:
            return 1
        if (n - 1) not in cache:
            cache[n-1] = self.steps_helper(n - 1, cache)
        if (n - 2) not in cache:
            cache[n-2] = self.steps_helper(n - 2, cache)
        return cache[n-1] + cache[n-2]


if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(10))
