class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans = []
        for op in tokens:
            if op not in "+-*/":
                ans.append(int(op))
            else:
                b = ans.pop()
                a = ans.pop()

                if op == '+':
                    ans.append(a + b)
                elif op == '-':
                    ans.append(a - b)
                elif op == '*':
                    ans.append(a * b)
                else: # op == '/'
                    ans.append(int(a / b))
            
        return ans[-1]