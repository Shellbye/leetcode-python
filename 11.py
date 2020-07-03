class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        left = 0
        right = len(height) - 1
        while left != right:
            ans = max(ans, (right - left) * min(height[left], height[right]))
            if height[left] <= height[right]:
                left = left + 1
            else:
                right = right - 1
        return ans

        # n^2
        # ans = 0
        # for i in range(len(height)):
        #     left = height[i]
        #     for j in range(i+1, len(height)):
        #         right = height[j]
        #         area = (j - i) * min(left, right)
        #         ans = max(ans, area)
        # return ans
