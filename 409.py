class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = {}
        for v in s:
            if v in m:
                m[v] = m[v] + 1
            else:
                m[v] = 1
        max_p = 0
        has_center = False
        # print(m)
        for k in m:
            if m[k] == 1 and not has_center:
                # print("put center:{}".format(k))
                max_p = max_p + 1
                has_center = True
                continue
            if m[k] % 2 == 0:
                # print("put double:{}".format(k))
                max_p = max_p + m[k]
            else:
                if has_center:
                    # print("put single without center:{}".format(k))
                    max_p = max_p + m[k] - 1
                else:
                    # print("put single with center:{}".format(k))
                    max_p = max_p + m[k]
                    has_center = True
        return max_p
