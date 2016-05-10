class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        min_price = 0
        if prices:
            min_price = prices[0]

        for i, price in enumerate(prices):
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit


if __name__ == '__main__':
    s = Solution()
    l = [19.35, 19.30, 18.88, 18.93, 18.95, 19.03, 19.00, 18.97, 18.97, 18.98]
    print(s.maxProfit(l))
