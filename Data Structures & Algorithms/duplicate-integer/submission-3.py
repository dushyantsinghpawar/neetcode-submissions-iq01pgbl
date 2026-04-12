class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsHash = {}
        for num in nums:
            if num in numsHash:
                return True
            numsHash[num] = 1
        return False