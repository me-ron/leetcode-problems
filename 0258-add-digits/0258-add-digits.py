class Solution:
    def addDigits(self, num: int) -> int:
        num2=[x for x in str(num)]
        num2=list(map(int,num2))
        while len(num2)!=1:
            x=sum(num2)
            num2=[x for x in str(x)]
            num2=list(map(int,num2))
        return num2[0]