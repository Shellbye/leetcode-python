class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = num
        while s > 9:
            # print("enter", s, num)
            tmp = 0
            while num and num % 10 >= 0:
                # print("enter==", tmp, num)
                tmp = tmp + num % 10
                num = num / 10
                # print("exit==", tmp, num)
            s = tmp + num
            num = s 
            # print("exit", s, num)
        return s
