class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return [1]
        L = len(digits) - 1
        digits[-1] = digits[-1] + 1
        acc = 0
        for i in range(L, -1, -1):
            digits[i] = digits[i] + acc
            if digits[i] >= 10:
                digits[i] = digits[i] - 10
                acc = 1
            else:
                return digits
        # print(digits)
        if acc:
            return [1] + digits
        return digits
