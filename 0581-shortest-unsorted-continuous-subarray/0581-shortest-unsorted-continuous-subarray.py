class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        end=-1
        max=nums[0]
        for i in range(1,len(nums)):
            if max>nums[i]:
                end=i
            else:
                max=nums[i]
        start=0
        min=nums[-1]
        for i in range(len(nums)-1,-1,-1):
            if min<nums[i]:
                start=i
            else:
                min=nums[i]
        return end-start+1