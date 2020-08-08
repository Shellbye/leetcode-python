class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(ransomNote) > len(magazine):
            return False
        r = list(ransomNote)
        m = list(magazine)
        r.sort()
        m.sort()
        m_index = 0
        for i in range(len(r)):
            while m_index < len(m) and r[i] != m[m_index]:
                m_index = m_index + 1
            if m_index >= len(m):
                return False
            m_index = m_index + 1
        return True


class SolutionV2(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        r_map = {}
        for c in ransomNote:
            if c in r_map:
                r_map[c] = r_map[c] + 1
            else:
                r_map[c] = 1
        m_map = {}
        for c in magazine:
            if c in m_map:
                m_map[c] = m_map[c] + 1
            else:
                m_map[c] = 1
        for c in r_map.keys():
            if c not in m_map:
                return False
            if r_map[c] > m_map[c]:
                return False
        return True
