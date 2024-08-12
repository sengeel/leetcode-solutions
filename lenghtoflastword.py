class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        s = s.rstrip()
        n = len(s)
        lenght = 0

        for i in range(n-1, -1, -1):
            if s[i] == ' ':
                break

            lenght +=1

        return lenght
