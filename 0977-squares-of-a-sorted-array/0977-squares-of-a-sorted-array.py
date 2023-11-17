class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i=0
        k=j=len(nums)-1
        num=[0]*len(nums)
        while i<=j:
            if abs(nums[i])>=abs(nums[j]):
                num[k]=nums[i]**2
                i+=1
            else:
                num[k]=nums[j]**2
                j-=1
            k-=1
        return num