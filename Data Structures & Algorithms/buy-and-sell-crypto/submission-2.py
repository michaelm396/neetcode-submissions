class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Find the max profit TWO POINTER
        #1. store change in proft from each day.
        #2. Largest profit is highest value in list - lowest value in list
        #3. return i of that element
        left = 0
        right = 1
        max_profit = 0
        while right < len(prices):
            buy = prices[left]
            sell = prices[right]
            if buy < sell:
                profit = sell - buy
                max_profit = max(max_profit,profit)
            else:
                left = right
            right+=1
        return max_profit