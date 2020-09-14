class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return False
        divider = set()
        divider.add(1)
        for i in range(2, int(math.sqrt(abs(num))) + 1):
            if i not in divider:
                if num % i == 0:
                    d = num / i 
                    # print(d, i)
                    divider.add(d)
                    divider.add(i)
        # print(divider)
        if num == sum(divider):
            return True
        return False

                    
