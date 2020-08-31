class Solution(object):
    line_0 = set('qwertyuiop')
    line_1 = set('asdfghjkl')
    line_2 = set('zxcvbnm')
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans = []
        for w0 in words:
            w = w0.lower()
            # print(w)
            if not w:
                ans.append(w0)
            i = 0
            if i < len(w) and w[i] in self.line_0:
                # print("line_0")
                while i < len(w) and w[i] in self.line_0:
                    i = i + 1
                # print("end at ", i)
                if i == len(w):
                    ans.append(w0)
            elif i < len(w) and w[i] in self.line_1:
                # print("line_1")
                while i < len(w) and w[i] in self.line_1:
                    i = i + 1
                # print("end at ", i)
                if i == len(w):
                    ans.append(w0)
            elif i < len(w) and w[i] in self.line_2:
                # print("line_2")
                while i < len(w) and w[i] in self.line_2:
                    i = i + 1
                # print("end at ", i)
                if i == len(w):
                    ans.append(w0)
            else:
                pass
        return ans
