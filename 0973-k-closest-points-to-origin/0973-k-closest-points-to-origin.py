class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dic = {}
        for i in range(len(points)):
            x=points[i][0]**2+points[i][1]**2
            dic[tuple(points[i])]=x
        def sorter(point):
            return dic[tuple(point)]
        points.sort(key = sorter)
        return points[:k]
        
        

        