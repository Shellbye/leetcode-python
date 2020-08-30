class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        for v in nums1:
            start = nums2.index(v)
            find = False
            for i in range(start, len(nums2)):
                if nums2[i] > v:
                    find = True
                    ans.append(nums2[i])
                    break
            if not find:
                ans.append(-1)
        return ans
