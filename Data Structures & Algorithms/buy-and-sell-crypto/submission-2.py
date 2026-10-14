class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1

        maxProf = 0

        while j < len(prices):
            buyL = prices[i]
            sellH = prices[j]
            if buyL < sellH :
                maxProf = max(maxProf, (sellH - buyL))
                j+= 1
            else:
                i = j
                j += 1

        return maxProf