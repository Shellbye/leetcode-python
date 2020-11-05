from collections import deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        ans = 1
        abc = list('abcdefghijklmnopqrstuvwxyz')
        queue = deque()
        queue.append(beginWord)
        visited = set([beginWord])
        while queue:
            cur_level_size = len(queue)
            for t in range(cur_level_size):
                w = queue.popleft()
                for i in range(len(w)):
                    for a in abc:
                        wlist = list(w)
                        wlist[i] = a 
                        wn = "".join(wlist)
                        if wn not in wordList:
                            continue
                        if wn == endWord:
                            # print("found")
                            return ans + 1
                        if wn not in visited:
                            visited.add(wn)
                            queue.append(wn)
                        # else:
                        #     print("dup")

            ans += 1
        return 0
