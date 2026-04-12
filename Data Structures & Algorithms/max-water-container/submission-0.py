class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxA = 0
        leftH = 0
        rightH = n - 1
        
        while leftH < rightH:
            H = min(heights[leftH], heights[rightH])
            W = rightH - leftH
            maxA = max(maxA, H * W)
            
            if heights[leftH] > heights[rightH]:
                rightH -= 1
            else:
                leftH += 1

        return maxA