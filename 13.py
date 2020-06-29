class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = i = 0
        while i < len(s):
            if s[i] == 'M':
                ans = ans + 1000
            elif s[i] == 'D':
                ans = ans + 500
            elif s[i] == 'L':
                ans = ans + 50
            elif s[i] == 'V':
                ans = ans + 5
            # I X C 
            elif s[i:i+2] == 'IV':
                ans = ans + 4
                i = i + 1
            elif s[i:i+2] == 'IX':
                ans = ans + 9
                i = i + 1
            elif s[i:i+2] == 'XL':
                ans = ans + 40
                i = i + 1
            elif s[i:i+2] == 'XC':
                ans = ans + 90
                i = i + 1
            elif s[i:i+2] == 'CD':
                ans = ans + 400
                i = i + 1
            elif s[i:i+2] == 'CM':
                ans = ans + 900
                i = i + 1
            elif s[i] == 'I':
                ans = ans + 1
            elif s[i] == 'X':
                ans = ans + 10
            elif s[i] == 'C':
                ans = ans + 100
            i = i + 1
        return ans
