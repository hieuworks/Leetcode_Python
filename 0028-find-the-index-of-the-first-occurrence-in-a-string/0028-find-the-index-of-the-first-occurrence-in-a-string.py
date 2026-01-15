class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lenHaystack = len(haystack)
        lenNeedle = len(needle)
        if lenNeedle == 0:
            return 0
        for i in range(lenHaystack): 
            #first check for the index of haystack whether that is similar to first character of needle
            if haystack[i] == needle[0] and i <= lenHaystack - lenNeedle:
                index = i
                charCorrectCount = 0
                for j in range(lenNeedle):
                    if haystack[index] == needle[j]:
                        index += 1
                        charCorrectCount +=1
                    if charCorrectCount == lenNeedle:
                        return i #return index of the first occurrence of needle in haystack
        return -1
                    
