class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        ans=nums[-1]
        for i in range (len(nums)-1):
            ans=min(nums[i+1] - nums[i],ans)
        return ans
        