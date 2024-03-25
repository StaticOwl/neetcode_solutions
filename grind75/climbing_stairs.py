#Fibonacci Sequence

class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        track = [0]*n
        track[0] = 1
        track[1] = 2
        for i in range (2, n):
            track[i] = track[i-1]+track[i-2]
        
        return track[-1]