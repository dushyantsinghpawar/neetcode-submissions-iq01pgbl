class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i, v in Counter(nums).items():
            if v > 1:
                return True
        return False