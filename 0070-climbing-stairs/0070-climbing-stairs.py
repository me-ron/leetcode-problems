class Solution:
    def climbStairs(self, n: int) -> int:
        if n in [0,1,2]:
            return n
        else:
            x=1
            y=2
            for i in range(2,n):
                ai=x+y
                x=y
                y=ai
            return ai        
