class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = float('inf')
        max_p = 0
        for value in prices:
            if value < min_p:
                min_p = value
            elif value - min_p > max_p:
                max_p = value - min_p
        return max_p

