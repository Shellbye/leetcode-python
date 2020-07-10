class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        low, high = 0, len(s) - 1
        # print("init", low, high)
        while low <= high:
            # print("while enter", low, high)
            while low < len(s) and not s[low].isalnum():
                low = low + 1
            while high >= 0 and not s[high].isalnum():
                high = high - 1
            if low < len(s) and high >= 0 and s[low] != s[high]:
                return False
            low = low + 1
            high = high - 1
            # print("while exit", low, high)
        return True
