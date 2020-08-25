class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        if len(houses) == 0:
            return 0
        if len(heaters) == 0:
            return 2147483647
        
        # 先计算需要覆盖的房屋范围
        # 房屋覆盖范围是个不好明确的概念，需要先计算供暖器之间的最大距离
        # 然后最小半径一定是小于这个最大距离的一半的
        # 在计算加热器之间的距离，房屋范围的边界也需要考虑
        houses.sort()
        heaters.sort()
        # max_d = heaters[0]
        # for i in range(1, len(heaters)):
        #     if heaters[i] - heaters[i - 1] > max_d:
        #         max_d = heaters[i] - heaters[i - 1]
        # max_r = max_d / 2

        ans = 0
        # 从房子的角度去找加热器
        for h in houses:
            # h 是房子的坐标，找距离这个坐标最近的加热器的坐标，计算距离
            if h in heaters:
                continue
            else:
                ans = max(ans, self.find(h, heaters))
        return ans

    def find(self, h, heaters):
        # print("find {} in {}".format(h, heaters))
        low = 0
        high = len(heaters) - 1
        min_r = abs(h - heaters[0])
        while low < high:
            mid = (high + low) / 2
            # print(low, mid, high)
            if heaters[mid] > h:
                high = mid - 1
            else:
                low = mid + 1
            # 记录
            d = abs(h - heaters[mid])
            d1 = abs(h - heaters[low])
            d2 = abs(h - heaters[high])
            min_r = min([min_r, d, d1, d2])
        # print(min_r)
        return min_r
