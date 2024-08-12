class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        R = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M': 1000}

        i = 0
        n = len(s)
        summ = 0

        while i < n:
            if i < n - 1 and R[s[i]] < R[s[i + 1]]:
                summ += R[s[i + 1]] - R[s[i]]
                i += 2

            else:
                summ += R[s[i]]
                i += 1
        return summ