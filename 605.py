class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        index = 0
        while index < len(flowerbed) and n > 0:
            if flowerbed[index] != 0:
                index += 1
                continue
            # leading 00
            if index == 0 and index + 1 < len(flowerbed) and flowerbed[index + 1] == 0:
                flowerbed[index] = 1
                n = n - 1
                index += 1
                continue
            # tailing 00
            if index == len(flowerbed) - 1 and flowerbed[index - 1] == 0:
                flowerbed[index] = 1
                n = n - 1
                index += 1
                continue
            # pre and after
            if flowerbed[index - 1] == 0 and flowerbed[index + 1] == 0:
                flowerbed[index] = 1
                n = n - 1
            index += 1
        # print(n)
        return n == 0
