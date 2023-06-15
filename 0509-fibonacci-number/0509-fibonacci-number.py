class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        else:
            x=0
            y=1
            ai=0
            for i in range (1,n):
                ai=x+y
                x=y
                y=ai
            return ai