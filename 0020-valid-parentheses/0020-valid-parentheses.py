class Solution:
    def isValid(self, s: str) -> bool:
        open_bracket1 = '('
        open_bracket2 = '['
        open_bracket3 = '{'
        close_bracket1 = ')'
        close_bracket2 = ']'
        close_bracket3 = '}'

        stack = []
        for i in range (len(s)):
            if s[i] == open_bracket1 or s[i] == open_bracket2 or s[i] == open_bracket3:
                stack.append(s[i])
            if s[i] == close_bracket1 or s[i] == close_bracket2 or s[i] == close_bracket3:
                if not stack:
                    return False
                top = stack.pop()
                if top == open_bracket1 and s[i] == close_bracket1:
                    pass
                elif top == open_bracket2 and s[i] == close_bracket2:
                    pass
                elif top == open_bracket3 and s[i] == close_bracket3:
                    pass
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False