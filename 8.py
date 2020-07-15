class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        ans = 0
        if s == '':
            return ans
        pt = 0
        # remove leading whitespace
        while pt < len(s) and s[pt] == " ":
            pt = pt + 1
        # check first non whitespace char
        if pt >= len(s):
            return ans
        first_c = s[pt]
        if not first_c.isdigit() and first_c != "+" and first_c != "-":
            return ans
        # deal with sign
        sign = 1
        if not first_c.isdigit():
            pt = pt + 1
            if first_c == "-":
                sign = -1
        # get the entire digit string
        start = pt
        end = pt
        while pt < len(s) and s[pt].isdigit():
            end = pt
            pt = pt + 1
        # check if digit is too big
        # if end - start + 1 > 10:
        #     if sign == 1:
        #         return 2147483647
        #     return -2147483648
        # do transfer
        digit = s[start:end+1]
        if not digit.isdigit():
            return ans
        ans = long(digit)
        if sign == 1 and ans > 2147483647:
            return 2147483647
        elif sign == -1 and ans > 2147483648:
            return -2147483648
        return ans * sign
