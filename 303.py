class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        L = len(nums)
        self.data = [0] * (L + 1)
        for i in range(L):
            self.data[i+1] = self.data[i] + nums[i]



    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.data[j+1] - self.data[i]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
