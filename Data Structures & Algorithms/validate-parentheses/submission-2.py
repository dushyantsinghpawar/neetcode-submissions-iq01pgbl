class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        stack = []
        
        for ch in s:
            if ch in "{[(":
                stack.append(ch)
            else:
                if not stack and ch in "}])":
                    return False
                
                if stack and ch == "]" and stack[-1] != "[":
                    return False
                elif stack and ch == "}" and stack[-1] != "{":
                    return False
                elif stack and ch == ")" and stack[-1] != "(":
                    return False
                
                stack.pop()

        return not stack

