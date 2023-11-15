class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        j=int(math.sqrt(c))
        if j*j==c:
            return True
        i=0
        while i<=j:
            sqr=i**2+j**2
            if sqr==c:
                return True
            elif sqr>c:
                j-=1
            else:
                i+=1
        return False