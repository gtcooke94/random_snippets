import math
from typing import List

# Idea: increasing day to day: hold
# Decreasing day to day: buy at min
# Idea: look forward until you see a decrease. Buy. Look forward until you see an increase. Sell


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        holding = False
        profit = 0
        hold_val = 0
        for i in range(len(prices)):
            if i == len(prices) - 1:
                if holding:
                    # if you're holding, it has to be increasing, so on the last day you want to sell
                    profit += prices[i] - hold_val
                continue
            if holding:
                # if I have stock
                if prices[i + 1] > prices[i]:
                    # increasing next - continue holding
                    continue
                elif prices[i + 1] < prices[i]:
                    # decreasing next, sell day i
                    holding = False
                    profit += prices[i] - hold_val
                    hold_val = 0
            else:
                # if I don't have stock
                if prices[i + 1] > prices[i]:
                    # increasing next? Buy now
                    holding = True
                    hold_val = prices[i]
                elif prices[i + 1] < prices[i]:
                    # decreasing next - don't buy now
                    continue
        return profit

    def __call__(self, n):
        return self.maxProfit(n)
