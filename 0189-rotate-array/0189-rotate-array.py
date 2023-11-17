class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k=k%len(nums)
        def reverse(num,i,j):
            l=i
            r=j-1
            while l<r:
                num[l],num[r]=num[r],num[l]
                l+=1
                r-=1
        i=0
        j=len(nums)
        k=j-k
        reverse(nums,i,k)
        reverse(nums,k,j)
        reverse(nums,i,j)
        
        
        