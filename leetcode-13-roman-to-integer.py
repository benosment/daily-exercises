class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        values = {'I': 1,
                  'V': 5,
                  'X': 10,
                  'L': 50,
                  'C': 100,
                  'D': 500,
                  'M': 1000,
                 }
        rank = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        total = 0
        old_rank = 100
        last_value = 0
        for symbol in list(s):
            current_rank = rank.index(symbol)
            if current_rank > old_rank:
                total += values[symbol]
                total -= 2 * last_value
            else:
                total += values[symbol]
            last_value = values[symbol]
            old_rank = current_rank
        return total

if __name__ == '__main__':
    s = Solution()
    #print(s.romanToInt("DCXXI"))
    print(s.romanToInt("MCMXCVI"))
