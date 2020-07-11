class Solution(object):
    ms = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    def reformatDate(self, date):
        """
        :type date: str
        :rtype: str
        """
        d, m, y = date.split(" ")
        
        d = d[:-2]
        if int(d) < 10:
            d = "0" + d
        m = self.ms.index(m) + 1
        if m < 10:
            m = "0"+str(m)
        return "{}-{}-{}".format(y, m, d)
