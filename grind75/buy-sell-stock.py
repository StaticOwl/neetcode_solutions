#719ms O(n) time is more but this is the best possible complexity
def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        head = float(inf)
        for price in prices:
            if head < price:
                profit = max(profit, price - head)
            else:
                head = price

        return profit

