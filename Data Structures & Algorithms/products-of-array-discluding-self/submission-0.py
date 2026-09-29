class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prod = 1
        
        zero = False
        ans = [0] * len(nums)
        
        if nums.count(0) >= 2: return ans
        
        for i in range(len(nums)):
            if nums[i] != 0:
                prod *= nums[i]
            else:
                zero = True
                zi = i

        for i in range(len(nums)):
            if zero:
                ans[zi] = prod
                return ans
            elif not zero and nums[i] != 0:
                ans[i] = prod // nums[i]

        return ans
