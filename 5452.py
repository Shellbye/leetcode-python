class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) <= 1:
            return True
        arr.sort()
        diff = arr[1] - arr[0]
        # print(diff)
        for i in range(1, len(arr) - 1):
            if arr[i+1] - arr[i] != diff:
                # print(arr[i], arr[i+1], diff)
                return False
        return True
