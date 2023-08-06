class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l=0
        i=0
        x=sum(nums)
        while i<len(nums):
            l+=nums[i]
            if (x-l)==l-nums[i]:
                break
            i+=1
        return i if i!=len(nums) else -1
            
            
            
        