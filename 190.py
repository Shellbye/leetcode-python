class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        o = str(bin(n))[2:][::-1]
        while len(o) < 32:
            o = o + "0"
        b = int(o, 2)
        return b 
