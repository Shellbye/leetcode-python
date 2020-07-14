class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        ans = []
        if numRows == 1:
            return s 

        l = 2 * numRows - 2
        for i in range(numRows):
            # get ith row
            if i % numRows == 0:
                # start point
                for idx in range(i, len(s), l):
                    ans.append(s[idx])
            elif i % numRows == numRows - 1:
                # end point
                for idx in range(i, len(s), l):
                    ans.append(s[idx])
            else:
                # middle point
                for idx in range(i, len(s), l):
                    # 向下的
                    ans.append(s[idx])
                    # 折行之后的 l-i + idx-i
                    af = l-2*i+idx
                    if af < len(s):
                        # print(idx,l,i,af)
                        ans.append(s[af])
        return "".join(ans)


class SolutionV2(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        ans = []
        if numRows == 1:
            return s 

        l = 2 * numRows - 2
        for i in range(numRows):
            for idx in range(i, len(s), l):
                ans.append(s[idx])
                if i != 0 and i != numRows - 1:
                    # 折行之后的索引 l-i + idx-i
                    af = l-i + idx-i
                    if af < len(s):
                        ans.append(s[af])
        return "".join(ans)
