class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ans = ""
        acc = 0

        num1 = num1[::-1]
        num2 = num2[::-1]
        L = max(len(num1), len(num2))
        for i in range(L+1):
            if i < len(num2):
                n2 = int(num2[i])
            else:
                n2 = 0
            if i < len(num1):
                n1 = int(num1[i])
            else:
                n1 = 0

            n = n1 + n2 + acc
            # print(i, n1, n2, acc)
            acc = 0
            if n > 9:
                n = n - 10
                acc = 1
            ans = str(n) + ans
        while ans and ans[0] == '0' and len(ans) > 1:
            ans = ans[1:]
        return ans
