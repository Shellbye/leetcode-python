class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        L = len(haystack)
        n = len(needle)
        p1 = 0
        while p1 < L - n + 1:  # avoid some useless compare
            if haystack[p1] == needle[0]:
                match_len = 1
                for j in range(1, n):
                    if p1 + j >= L:
                        break
                    if haystack[p1+j] != needle[j]:
                        break
                    match_len = j + 1
                if match_len == n:
                    return p1
            p1 = p1 + 1
        return -1
