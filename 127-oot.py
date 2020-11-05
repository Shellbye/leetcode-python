class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        ab = list(set("".join(wordList)))
        # print("ab:{}".format(ab))
        path_list = []
        path = [beginWord]
        self.bfs(0, ab, endWord, wordList, path, path_list)
        if len(path_list) < 1:
            return 0
        min_len = len(path_list[0])
        for p in path_list:
            min_len = min(min_len, len(p))
        return min_len

    def bfs(self, idx, ab, endWord, wordList, path, path_list):
        # print("bfs, idx:{}, path:{}".format(idx, path))
        for i in range(len(path[-1])):
            for alpha in ab:
                b = list(path[-1])
                b[i] = alpha
                bw = "".join(b)
                if bw == endWord:
                    path += [endWord]
                    path_list.append(path[:])
                    # print("reach one end with path_list:{}".format(path_list))
                    return
                if bw not in wordList:
                    continue
                if bw in path:
                    continue
                # print("bw:{} in wordList".format(bw))
                self.bfs(i + 1, ab, endWord, wordList, path + [bw], path_list)
