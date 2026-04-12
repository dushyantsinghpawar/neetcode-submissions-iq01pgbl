class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        stack = []
        for ch in s:
            if not stack and ch in "}])":
                return False
            
            if stack and ch == "]" and stack[-1] == "[":
                stack.pop()
            elif stack and ch == "}" and stack[-1] == "{":
                stack.pop()
            elif stack and ch == ")" and stack[-1] == "(":
                stack.pop()
            else: stack.append(ch)
        return False if stack else True

