class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        j=i+1
        while i<len(set(nums)):
            while j<len(nums):
                if nums[j]>nums[i]:
                    nums[i+1],nums[j]=nums[j],nums[i+1]
                    break
                j+=1
            i+=1
        return len(set(nums))
        