class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        cur = -1
        L = len(numbers) - 1
        ans = []
        while cur < L:
            cur = cur + 1
            # print("cur", cur)
            ans.append(cur + 1)
            to_find = target - numbers[cur]
            low, high = cur+1, L
            mid = (low + high) / 2
            while low <= high:
                mid = (low + high) / 2
                # print("low", low, "high", high, "mid", mid)
                if numbers[mid] == to_find:
                    ans.append(mid + 1)
                    return ans
                elif numbers[mid] < to_find:
                    low = mid + 1
                else:
                    high = mid - 1
            ans = []
        return ans


class SolutionV2(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        low = 0
        high = len(numbers) - 1
        while low < high:
            n = numbers[high] + numbers[low]
            if n == target:
                break
            elif n < target:
                low = low + 1
            else:
                high = high - 1
        return [low+1, high+1]
