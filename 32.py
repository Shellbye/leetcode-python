class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_valid_len = 0
        s0 = [1] * len(s)
        stack = []
        for i, c in enumerate(s):
            if c == "(" or len(stack) == 0:
                stack.extend([i, c])
            else:
                if stack[-1] == "(":
                    s0[i] = 0
                    stack.pop()
                    idx = stack.pop()
                    s0[idx] = 0
                else:
                    stack.extend([i, c])  # unmatch )
        z_count = max_z_count = 0
        for c in s0:
            if c == 0:
                z_count += 1
                max_z_count = max(max_z_count, z_count)
            else:
                z_count = 0
        return max_z_count
