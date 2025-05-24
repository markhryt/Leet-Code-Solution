class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        total = 0

        for i in range(len(s)-1):
            current = m[s[i]]
            nxt = m[s[i+1]]
            if current < nxt:
                total -= current
            else: 
                total += current
        
        total += m[s[-1]]

        return total


