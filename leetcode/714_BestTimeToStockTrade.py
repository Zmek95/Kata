from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        prices_len = len(prices)
        hold = [0] * prices_len
        free = [0] * prices_len

        # Have to buy stock on first day to hold
        hold[0] = -prices[0]

        for price_idx in range(1,prices_len):
            hold[price_idx] = max(hold[price_idx - 1], free[price_idx - 1] - prices[price_idx])
            free[price_idx] = max(free[price_idx - 1], hold[price_idx - 1] + prices[price_idx] - fee)
        
        # Return max profit from free since there is no point in holding stock on last day
        return free[-1]  
    

class TestClass:

    def test_one(self):
        input_1 = [1,3,2,8,4,9]
        input_2 = 2
        test = Solution()
        assert test.maxProfit(input_1, input_2) == 8


    def test_two(self):
        input_1 = [1,3,7,5,10,3]
        input_2 = 3
        test = Solution()
        assert test.maxProfit(input_1, input_2) == 6