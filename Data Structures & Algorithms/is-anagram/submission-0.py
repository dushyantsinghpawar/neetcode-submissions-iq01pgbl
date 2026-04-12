class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hS = {chr(97 + i): 0 for i in range(26)}
        hT = {chr(97 + i): 0 for i in range(26)}
        
        m, n = len(s), len(t)

        if m != n: return False

        for i in range(m):
            if s[i] not in hS:
                hS[s[i]] = 1
            hS[s[i]] += 1
            
            if t[i] not in hT:
                hT[t[i]] = 1
            hT[t[i]] += 1

        return hT == hS