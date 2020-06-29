class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k_array = []
        k_max = float('inf')
        for v in nums:
            # k array still has place
            if len(k_array) < k:
                k_array.append(v)
                k_max = min(k_max, v)
                continue
            # k array is full
            if v > k_max:
                k_array.remove(k_max)
                k_array.append(v)
                k_max = min(k_array)
        return k_max
