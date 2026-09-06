class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit=0
        lowest= prices[0]

        for i in prices:
            if i<lowest:
                lowest=i
            if i-lowest>maxProfit:
                maxProfit=i-lowest

        return maxProfit