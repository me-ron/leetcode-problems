class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n=len(names)
        for i in range (n):
            for j in range (i,n):
                if heights[j]>heights[i]:
                    heights[j],heights[i]=heights[i],heights[j]
                    names[j],names[i]=names[i],names[j]
        return names
        