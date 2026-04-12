class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        n = len(s)
        start = 0
        ans = 0
        for end in range(n):
            while s[end] in seen:
                seen.remove(s[start])
                start += 1
            seen.add(s[end])
            ans = max(ans, end - start + 1)
        return ans