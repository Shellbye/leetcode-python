class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        prime = [True] * n
        count = 0
        for i in range(2, n):
            if not prime[i]:
                continue
            count = count + 1
            k = i
            while k * i < n:
                prime[k*i] = False
                k = k + 1
        return count
