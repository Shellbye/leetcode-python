class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        0x100000000
        """
        # 2^32
        MASK = 0x100000000
        # 整型最大值
        MAX_INT = 0x7FFFFFFF
        MIN_INT = MAX_INT + 1
        while b != 0:
            carry = (a & b) << 1
            # print(a,b,carry)
            a = (a ^ b) % MASK
            b = carry % MASK
        if a < MAX_INT:
            return a
        print(a)
        # a ^ 0xFFFFFFFF 把 a 的前面都变成 0，后面的不少1和0也反了，所以需要
        # ～ 
        return ~(a ^ 0xFFFFFFFF) # ???
