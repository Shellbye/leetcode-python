class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        n = max(len(a), len(b))
        acc = 0
        ans = ''
        for i in range(n):
            if i < len(a):
                acc = acc + int(a[len(a) - i - 1])
            if i < len(b):
                acc = acc + int(b[len(b) - i - 1])
            s = acc % 2
            acc = acc / 2
            ans = ans + str(s)
        if acc:
            ans = ans + str(acc)
        return ans[::-1]
