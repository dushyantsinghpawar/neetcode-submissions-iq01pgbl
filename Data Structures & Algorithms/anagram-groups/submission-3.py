class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans = defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            for i in s:
                count[ord(i) - ord('a')] += 1

            key = tuple(count)
            ans[key].append(s)

        return list(ans.values())