class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        low, high = 0, len(s) - 1
        while low < high:
            while low < len(s) - 1 and s[low] not in 'aeiouAEIOU':
                low = low + 1
            while high > 0 and s[high] not in 'aeiouAEIOU':
                high = high - 1
            if low >= high:
                break
            tmp = s[low]
            s[low] = s[high]
            s[high] = tmp
            low = low + 1
            high = high - 1
        return "".join(s)
