class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        check = sorted(count, key=lambda x: -count[x])
        return check[:k]