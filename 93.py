class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s.isdigit():
            return []
        ans = []
        self.dfs(s, 0, [], ans, 0)
        return ans
    
    def dfs(self, s, idx, path, ans, fg_cnt):
        if len(path) > 4 or fg_cnt > 4 or idx > len(s):
            return
        # print(path, idx, fg_cnt)
        if self.is_valid_ip(path):
            ans.append(".".join(path))
            return 
        for i in range(3):
            f = s[idx:idx + 1 + i]
            # print("f:{} when fg_count:{}".format(f, fg_cnt))
            if not self.is_valid_frag(f):
                # print("{} not valid frag".format(f))
                continue
            
            if (len(s) - (idx + 1 + i)) > 3 * (3 - fg_cnt):
                # print("pre too small", f, "left len: {}".format(len(s) - (idx + 1 + i)))
                continue
            
            # print("new path:{}".format(path + [f]))
            self.dfs(s, idx + 1 + i, path + [f], ans, fg_cnt + 1)

    def is_valid_frag(self, f):
        if not f.isdigit():
            return False
        if len(f) > 1 and f[0] == "0":
            return False
        if int(f) < 0 or int(f) > 255:
            return False
        return True
    
    def is_valid_ip(self, path):
        frag = path
        if len(frag) != 4:
            return False
        for f in frag:
            if not self.is_valid_frag(f):
                return False
        return True
