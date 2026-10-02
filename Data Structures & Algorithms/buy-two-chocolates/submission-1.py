class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        n = len(prices)
        for j in range(n - 1):
            for i in range(n - 1 - j):
                if prices[i] > prices[i + 1]:
                    temp = prices[i]
                    prices[i] = prices[i + 1]
                    prices[i + 1] = temp

        cost = prices[0] + prices[1]
        if money >= cost:
            return money - cost
        return money
