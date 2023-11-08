class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def sorter(point):
            x=point[0]**2+point[1]**2
            return x
        points.sort(key = sorter)
        return points[:k]
        
        

        