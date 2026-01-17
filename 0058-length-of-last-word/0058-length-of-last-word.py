class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = -1
        if s == "":
            return 0
        while abs(i) <= len(s) and s[i] == ' ': #tim tu trong string khac ' ' 
            i -= 1
        count = 0
        while abs(i) <= len(s) and s[i] != ' ':
            count += 1
            i -= 1 
        return count
