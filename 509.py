class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        f = [0, 1]
        i = 2
        while i <= N:
            f.append(f[i-1] +f[i-2])
            i = i + 1
        return f[N]
