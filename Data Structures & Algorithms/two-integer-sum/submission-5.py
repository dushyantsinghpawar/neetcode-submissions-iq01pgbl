class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash_map = {}

        for i in range(len(nums)):
            comp = target - nums[i]

            if comp in hash_map: return [hash_map[comp], i]

            hash_map[nums[i]] = i

        return [] 