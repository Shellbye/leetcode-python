class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        ab_map = {}
        for a in A:
            for b in B:
                s = a + b 
                if s in ab_map:
                    ab_map[s] += 1
                else:
                    ab_map[s] = 1
        ans = 0
        for c in C:
            for d in D:
                s = c + d 
                if -s in ab_map:
                    ans += ab_map[-s]
        return ans



        """ timeout
        ans = 0
        for v in A:
            target3 = 0 - v
            cnt3 = self.threeSumCount(B, C, D, target3)
            ans += cnt3
        return ans
    
    def threeSumCount(self, B, C, D, target3):
        ans3 = 0
        for v in B:
            target2 = target3 - v
            cnt2 = self.twoSumCount(C, D, target2)
            ans3 += cnt2
        return ans3
    
    def twoSumCount(self, C, D, target2):
        ans2 = 0
        for v in C:
            target1 = target2 - v
            ans2 += D.count(target1)
        return ans2
        """
