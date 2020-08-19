class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        w_idx = 0
        r_idx = 0
        c_chr = 0
        cnt = 1
        for r_idx, c in enumerate(chars):
            if r_idx + 1 == len(chars) or chars[r_idx + 1] != c:
                # write
                chars[w_idx] = chars[c_chr]
                w_idx = w_idx + 1
                if cnt > 1:
                    for s in str(cnt):
                        chars[w_idx] = s
                        w_idx = w_idx + 1
            # print(c, cnt, w_idx, r_idx)
                c_chr = r_idx+1
                cnt = 1
            else:
                cnt = cnt + 1
        return w_idx
