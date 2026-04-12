class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        pospd = sorted(zip(position, speed))
        time = [float((target - p)/s) for p,s in pospd]
        ans = 0
        while len(time) > 1:
            front = time.pop()
            if time[-1] > front: ans += 1
            else: time[-1] = front         
        return ans + bool(time)