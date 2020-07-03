class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        max_len = 0
        max_str = s[0]
        for i in range(len(s)):
            # print("center on i:{}, s[i]:{}".format(i, s[i]))
            j = 0
            while i - j >= 0 and i + j < len(s) and s[i-j] == s[i+j]:
                if 2 * j > max_len:
                    # print("find new2 max, from {} to {}".format(i-j, i+j))
                    max_len = 2 * j
                    max_str = s[i-j:i+j+1]
                j = j + 1
            
            # print("side on i:{}, s[i]:{}".format(i, s[i]))
            j = 0
            while i - j + 1 >= 0 and i - j + 1 < len(s) and i + j < len(s) and s[i-j+1] == s[i+j]:
                if 2 * j - 1 > max_len:
                    # print("find new max, from {} to {}".format(i-j+1, i+j))
                    max_len = 2 * j - 1
                    max_str = s[i-j+1:i+j+1]
                j = j + 1
        return max_str
