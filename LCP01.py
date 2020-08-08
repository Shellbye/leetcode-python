class Solution(object):
    def game(self, guess, answer):
        """
        :type guess: List[int]
        :type answer: List[int]
        :rtype: int
        """
        ans = 0
        if guess[0] == answer[0]:
            ans = ans + 1
        if guess[1] == answer[1]:
            ans = ans + 1
        if guess[2] == answer[2]:
            ans = ans + 1
        return ans
