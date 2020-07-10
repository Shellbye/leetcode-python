class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        last_row = [1,2,1]
        k_row = []
        for i in range(3, rowIndex+1):
            k_row = [1]
            for j in range(1, i):
                k_row.append(last_row[j-1] + last_row[j])
            k_row.append(1)
            last_row = k_row
        return last_row
