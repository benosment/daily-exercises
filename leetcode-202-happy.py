class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        d = {}
        return happy_helper(n, d)

def happy_helper(n, d):
    if n in d:
       return False
    d[n] = 1
    val = 0
    while n:
       lowest = n % 10
       val += lowest * lowest
       n -= lowest
       n /= 10
    if val == 1:
       return True
    else:
       return happy_helper(val, d)


if __name__ == '__main__':
    s = Solution()
    print(s.isHappy(19))
    print(s.isHappy(82))
    print(s.isHappy(8))
