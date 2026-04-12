class Solution:
    def wordMap(self, word: str) -> dict:
        w_map = {chr(i): 0 for i in range(97, 123)}
        for w in word:
            w_map[w] += 1
        return w_map
    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        n = len(s2)
        
        if window > n:
            return False
            
        for i in range(n - window + 1):
            if self.wordMap(s1) == self.wordMap(s2[i :  i + window]):
                return True
        return False
        