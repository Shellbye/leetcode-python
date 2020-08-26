class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 2:
            return False
        if len(s) == 2 and s[0] == s[1]:
            return True
        if len(s) == 3 and s[0] == s[1] and s[0] == s[2]:
            return True
        checked_substr = []
        for i in range(2, len(s) / 2 + 1):
            # print("字符串长度 {}, 当前检查子串 {}".format(len(s), i))
            if len(s) % i == 0:
                sub_len = len(s) / i
                # print("字符串长度是 {} 的倍数, 要比较的子串长度是 {}".format(i, sub_len))
                is_repeated = True
                for j in range(sub_len):
                    cnt = 1
                    while is_repeated and cnt < i and j + sub_len * cnt < len(s):
                        if s[j] == s[j + sub_len * cnt]:
                            cnt = cnt + 1
                            continue
                        is_repeated = False
                if is_repeated:
                    return True
        rep = True
        v0 = s[0]
        for v in s:
            if v != v0:
                rep = False
        return rep
