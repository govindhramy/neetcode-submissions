class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minima = None
        maxima = None

        ans = 0

        for p in prices:
            if minima is None or p < minima:
                minima = p
                maxima = None
            elif maxima is None or p > maxima:
                maxima = p
                ans = max(ans, maxima - minima)
        return ans
            