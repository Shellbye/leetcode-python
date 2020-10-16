class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        任何大数和前面的小数交换都会导致变大，所以最大的定义就是每一个数都比它后面的大
        最小的定义刚好相反
        从后往前，找到一个比后面的数 小 的一个数 lit，
        然后找 lit 后面比它大的哪些数，找到其中最小的一个 big，和它对调
        然后 big 的新位置后面的要排序，通过排序保证最小
        [4,2,0,2,3,2,0]
        [3,2,1]
        [1,3,2]
        [1,2,3]
        [1,1,5]
        [1,2]
        """
        L = len(nums)
        
        lit = lit_idx = None
        for i in range(L):
            for j in range(i, L):
                if nums[i] < nums[j] and i > lit_idx:
                    lit_idx = i
                    lit = nums[i]
        # print(lit, lit_idx)
        if lit is None:
            nums.sort()
            return

        big = big_idx = float('inf')
        for j in range(lit_idx, L):
            # print("j, ", j, nums[j], "big, ", big)
            if nums[j] > lit and nums[j] < big:
                big = nums[j]
                big_idx = j
        # print(big, big_idx)
        nums[lit_idx], nums[big_idx] = nums[big_idx], nums[lit_idx]
        nums[lit_idx + 1:] = sorted(nums[lit_idx + 1:])
