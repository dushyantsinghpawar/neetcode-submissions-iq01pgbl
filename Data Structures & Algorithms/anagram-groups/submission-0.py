class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_set = {}
        for s in strs:
            key = frozenset(Counter(s).items())
            hash_set.setdefault(key, []).append(s)
        # print(hash_set)

        return [val for _, val in hash_set.items()]