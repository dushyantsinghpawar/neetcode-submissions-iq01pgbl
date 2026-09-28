class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {chr(97 + i) : 0 for i in range(26)}
        t_dict = {chr(97 + i) : 0 for i in range(26)}

        if len(s) != len(t): return False

        for i in range(len(s)):
            s_dict[s[i]] += 1
            t_dict[t[i]] += 1

        return s_dict == t_dict