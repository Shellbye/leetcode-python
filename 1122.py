class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        ans = []
        for v in arr2:
            ans += [v] * arr1.count(v)

        dif = [v for v in arr1 if v not in arr2 ]
        dif.sort()
        return ans + dif
        
