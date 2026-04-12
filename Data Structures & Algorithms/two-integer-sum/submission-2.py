class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_set = {val: key for key, val in enumerate(nums)}
        for i in range(len(nums)):
            if (target - nums[i]) in hash_set and i != hash_set[target - nums[i]]:
                return [min(i, hash_set[target - nums[i]]), max(i, hash_set[target - nums[i]])]