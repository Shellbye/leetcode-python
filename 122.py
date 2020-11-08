class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans = 0
        idx = 0
        while idx < len(prices):
            if idx + 1 < len(prices) and prices[idx] < prices[idx + 1]:
                buy_idx = idx
                out_idx = idx + 1
                while out_idx + 1 < len(prices) and prices[out_idx] < prices[out_idx + 1]:
                    out_idx += 1
                ans += prices[out_idx] - prices[buy_idx]
                idx = out_idx + 1
            else:
                idx += 1
        return ans
