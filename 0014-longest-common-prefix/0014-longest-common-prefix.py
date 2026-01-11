class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word = strs[0]
        prefix = ""
        for i in range(len(first_word)): #duyệt từng từ trong first_word
            char = first_word[i]        
            for next_word in strs[1:]:   #so sánh từ trong first_word với từ ở vị trí tương ứng 
                if len(next_word) <= i or char != next_word[i]:
                    return prefix
            prefix += char
        return prefix
        