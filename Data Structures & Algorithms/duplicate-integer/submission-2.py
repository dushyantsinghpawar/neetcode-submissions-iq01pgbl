class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsHash = {}
        for num in nums:
            if num not in numsHash:
                numsHash[num] = 1
            else:
                return True
        return False