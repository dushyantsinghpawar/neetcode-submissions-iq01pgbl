class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        i, j = 0, n - 1
        water = 0
        lH_max = rH_max = 0

        while i < j:
            if height[i] > height[j]:
                if rH_max <= height[j]:
                    rH_max = height[j]
                else:
                    water += rH_max - height[j]
                j -= 1
            else: # height[i] <= height[j]
                if lH_max <= height[i]:
                    lH_max = height[i]
                else:
                    water += lH_max - height[i]
                i += 1
        
        return water