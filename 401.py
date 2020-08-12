class Solution(object):
    ans = set()

    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        if num >= 9 or num < 0:
            return self.ans
        self.backtrack(num, [0]*10)
        a = list(self.ans)
        a.sort()
        return a 
    
    def backtrack(self, num, track):
        # print("enter backtrack with num:{} track:{}".format(num, track))
        if sum(track) == num:
            # back track reach leaf, check and return
            valid, time = self.is_valid_time(track)
            if valid:
                self.ans.add(time)
            return
        for i in range(len(track)):
            if track[i] == 1:
                continue
            track[i] = 1
            # print("goto next with:{}".format(track))
            self.backtrack(num, track)
            # print("return and remove")
            track[i] = 0

    def is_valid_time(self, track):
        hour = 8 * track[0] + 4 * track[1] + 2 * track[2] + 1* track[3]
        minu = 32 * track[4] + 16 * track[5] + 8 * track[6] + 4 * track[7] + 2 * track[8] + 1 * track[9]
        valid = hour < 12 and minu < 60
        if minu < 10:
            minu_str = "0" + str(minu)
        else:
            minu_str = str(minu)
        time = str(hour) + ":" + minu_str
        return valid, time
