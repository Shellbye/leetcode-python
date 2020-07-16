class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        def gen(s, left_cnt, right_cnt):
            # print(s, left_cnt, right_cnt)
            if left_cnt == 0 and right_cnt == 0:
                # print(s)
                # print("get:", s)
                ans.append(s)
                return
            if left_cnt > 0:
                gen(s + "(", left_cnt - 1, right_cnt)
            if right_cnt > left_cnt:
                gen(s + ")", left_cnt, right_cnt - 1)
            else:
                # print("right_cnt less than left_cnt")
                return
        gen("", n, n)
        return ans
