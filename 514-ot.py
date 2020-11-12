class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        # "nyngl"
          "yyynnnnnnlllggg"
        # "caotmcaataijjxi"
          "oatjiioicitatajtijciocjcaaxaaatmctxamacaamjjx"
        # "caotmcaataijjxi"
          "oatjiioicitatajt"
        # "caotmcaataijjxi"
          "ioicitatajt"
        """
        ans = set()
        pre_point = 0
        self.do_calc(pre_point, ring, key, 0, [], ans)
        # print(ans)
        return min(ans) + len(key)

    def do_calc(self, pre_point, ring, key, i, step_path, ans):
        if i == len(key):
            ans.add(sum(step_path))
            return 
        k = key[i]
        start_point = pre_point
        steps = 0
        while start_point + steps < len(ring) or start_point - steps >= 0:
            asc = (start_point + steps) % len(ring)
            dsc = (start_point - steps) % len(ring)
            # 不光需要前后一致的，不一致的也需要
            if ring[asc] == k:
                # print("start from:{} find {} at {} with {} steps".format(start_point, k, asc, steps))
                self.do_calc(asc, ring, key, i + 1, step_path + [steps], ans)
                # return 
            if ring[dsc] == k:
                # print("start from:{} find {} at {} with {} steps".format(start_point, k, dsc, steps))
                self.do_calc(dsc, ring, key, i + 1, step_path + [steps], ans)
                # return 
            steps += 1
