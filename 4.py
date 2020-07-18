class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1, l2 = len(nums1), len(nums2)
        # if l1 == 0:
        #     if l2 % 2 == 0:
        #         return (nums2[l2 / 2 - 1] + nums2[l2 / 2 + 1 - 1]) / 2
        #     else:
        #         return nums2[l2 / 2]
        # elif l2 == 0:
        #     if l1 % 2 == 0:
        #         return (nums1[l1 / 2 - 1] + nums1[l1 / 2 + 1 - 1]) / 2
        #     else:
        #         return nums1[l1 / 2]
        # 处理同时非空情况
        last_mid = (l1 + l2) / 2
        print("last_mid", last_mid)
        steps = 0
        m0 = m1 = -1
        p1, p2 = 0, 0
        while steps <= last_mid:
            # print("steps:{},p1:{},p2:{},m0:{},m1:{}".format(steps, p1, p2, m0, m1))
            m0 = m1
            if p1 < l1 and (p2 >= l2 or nums1[p1] < nums2[p2]) :
                # print("update p1")
                m1 = nums1[p1]
                p1 = p1 + 1
            else:
                # print("update p2")
                m1 = nums2[p2]
                p2 = p2 + 1
            steps = steps + 1
        # print("===steps:{},p1:{},p2:{},m0:{},m1:{}".format(steps, p1, p2, m0, m1))
        m = m1
        # print("m", m)
        if (l1 + l2) % 2 == 0:
            # print("update m", m)
            m = (m0 + m1) / 2.0
        return m
