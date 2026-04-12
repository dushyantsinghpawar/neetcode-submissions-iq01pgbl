class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        ans = [0] * n
        
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                temp_diff = i - stack[-1]
                ans[stack.pop()] = temp_diff
            stack.append(i)
        return ans
         