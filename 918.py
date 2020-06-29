class Solution(object):
    """https://leetcode-cn.com/problems/maximum-sum-circular-subarray/
    给定一个由整数数组 A 表示的环形数组 C，求 C 的非空子数组的最大可能和。

    在此处，环形数组意味着数组的末端将会与开头相连呈环状。
    （形式上，当0 <= i < A.length 时 C[i] = A[i]，而当 i >= 0 时 C[i+A.length] = C[i]）

    此外，子数组最多只能包含固定缓冲区 A 中的每个元素一次。
    （形式上，对于子数组 C[i], C[i+1], ..., C[j]，不存在 i <= k1, k2 <= j 其中 k1 % A.length = k2 % A.length）

    示例 1：
    输入：[1,-2,3,-2]
    输出：3
    解释：从子数组 [3] 得到最大和 3

    示例 2：
    输入：[5,-3,5]
    输出：10
    解释：从子数组 [5,5] 得到最大和 5 + 5 = 10
    示例 3：

    输入：[3,-1,2,-1]
    输出：4
    解释：从子数组 [2,-1,3] 得到最大和 2 + (-1) + 3 = 4
    示例 4：

    输入：[3,-2,2,-3]
    输出：3
    解释：从子数组 [3] 和 [3,-2,2] 都可以得到最大和 3
    示例 5：

    输入：[-2,-3,-1]
    输出：-1
    解释：从子数组 [-1] 得到最大和 -1

    提示：
    -30000 <= A[i] <= 30000
    1 <= A.length <= 30000
    """

    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # find non-circular min_sum
        min_sum = cur_sum = float('inf')
        for v in A[1:-1]:
            if cur_sum > 0:
                cur_sum = v
            else:
                cur_sum = cur_sum + v
            min_sum = min(min_sum, cur_sum)
        # print("min_sum:{}".format(min_sum))
        # print("circular max_sum:{}".format(sum(A) - min_sum))
        # find non-circular max_sum
        max_sum = cur_sum = A[0]
        for v in A[1:]:
            if cur_sum < 0:
                cur_sum = v
            else:
                cur_sum = cur_sum + v
            max_sum = max(max_sum, cur_sum)
        return max(max_sum, sum(A) - min_sum)


if __name__ == "__main__":
    A6 = [9, -4, -7, 9]
    r6 = Solution().maxSubarraySumCircular(A6)
    print(r6)
    assert r6 == 18

    A5 = [-2]
    r5 = Solution().maxSubarraySumCircular(A5)
    print(r5)
    assert r5 == -2

    A4 = [-2, -3, -1]
    r4 = Solution().maxSubarraySumCircular(A4)
    print(r4)
    assert r4 == -1

    A3 = [3, -2, 2, -3]
    r3 = Solution().maxSubarraySumCircular(A3)
    print(r3)
    assert r3 == 3

    A2 = [5, -3, 5]
    r2 = Solution().maxSubarraySumCircular(A2)
    print(r2)
    assert r2 == 10

    A1 = [1, -2, 3, -2]  # 3
    r1 = Solution().maxSubarraySumCircular(A1)
    print(r1)
    assert r1 == 3

    A0 = [3, -1, 2, -1]  # 4
    r0 = Solution().maxSubarraySumCircular(A0)
    print(r0)
    assert r0 == 4
