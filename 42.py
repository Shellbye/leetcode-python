class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        从第 1 个数字开始，分别计算它比左右两边低多少，如果相等，则计算平移动，最后乘以移动距离；
        循环直到 没有哪个位置比两边都低
        [0,1,0,2,1,0,1,3,2,1,2,1]

        """
        ans = 0
        cnt = 10
        changed = True
        while changed:
            i = 1
            # print("start round, {}".format(height))
            changed = False
            while i < len(height) - 1:
                # print(height[i])
                pre, nxt = i - 1, i + 1
                while pre > 0 and height[i] == height[pre]:
                    pre -= 1
                while nxt < len(height) - 1 and height[i] == height[nxt]:
                    nxt += 1
                    i += 1
                if height[i] < height[pre] and height[i] < height[nxt]:
                    changed = True
                    cap_h = min(height[pre], height[nxt]) - height[i]
                    cap = cap_h * (nxt - pre - 1)
                    ans += cap
                    for j in range(pre + 1, nxt):
                        # print("fill {} with {}".format(j, cap_h))
                        height[j] += cap_h  # 接满
                    # print("pos {} takes {}".format(i, cap))
                i += 1
            # print("round over")
        return ans
