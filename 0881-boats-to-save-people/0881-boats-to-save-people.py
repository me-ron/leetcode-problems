class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats=0
        i=0
        j=len(people)-1
        while i<=j:
            ans=people[i]+people[j]
            if ans<=limit:
                boats+=1
                i+=1
                j-=1
            else:
                boats+=1
                j-=1
        return boats