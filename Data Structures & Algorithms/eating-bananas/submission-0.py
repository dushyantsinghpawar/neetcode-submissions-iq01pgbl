class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        start, end = 1, max(piles)
        ans = end

        while start <= end:
            mid = (start + end) // 2
            
            rate = 0
            for b in piles:
                rate += (b + mid - 1) // mid # equal to ceil(b / mid)
            if rate <= h:
                ans = mid
                end = mid - 1
            else:
                start = mid + 1
        return ans