class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        primes = prime_numbers(num)
        primes = set(primes)
        if 2 in primes:
            primes.remove(2)
        if 3 in primes:
            primes.remove(3)
        if 5 in primes:
            primes.remove(5)
        return len(primes) == 0

def prime_numbers(n):
    primes = []
    i = 2
    while i*i <= n:
        if n % i == 0:
           primes.append(i)
           n = n / i
        else:
           i = i + 1
    if n > 0:
       primes.append(n)
    return primes

if __name__ == '__main__':
    s = Solution()
    print(s.isUgly(8))
    print(s.isUgly(14))
