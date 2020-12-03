class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 0
        none_list = set({1})
        
        for v in range(2, n):
            if v in none_list:
                continue
            i = 2
            while v * i < n:
                none_list.add(v * i)
                i += 1
        # print(none_list)
        return n - 1 - len(none_list)
