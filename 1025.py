class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        1 false
        2 true
        3 false 给对手呈现 2
        4 true 给对手呈现 3
        5 false 给对手呈现 4
        6 true 给对手呈现 3
        7 false 
        8 true
        """
        return N % 2 == 0
