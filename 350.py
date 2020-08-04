class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        for v in nums1:
            if v in nums2:
                if v in ans:
                    continue
                ans.extend([v] * min(nums1.count(v), nums2.count(v)))
        return ans
