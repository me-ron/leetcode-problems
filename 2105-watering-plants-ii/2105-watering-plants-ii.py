class Solution:
    def minimumRefill(self, plants: List[int], capA: int, capB: int) -> int:
        x,y = capA, capB
        i =0
        j = len(plants)-1
        refill = 0
        while i<=j:
            if i==j:
                if max(capA, capB)<plants[i]:
                    refill+=1
            else:
                if capA >= plants[i]:
                    capA-=plants[i]
                else:
                    refill+=1
                    capA = x
                    capA-=plants[i]
                if capB >= plants[j]:
                    capB-=plants[j]
                else:
                    refill+=1
                    capB = y
                    capB-=plants[j]
            i+=1
            j-=1
       
        return refill