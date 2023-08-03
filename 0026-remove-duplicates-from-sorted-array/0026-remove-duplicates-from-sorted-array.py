class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        while i<len(set(nums)):
            j=i+1
            while j<len(nums):
                if nums[j]>nums[i]:
                    nums[i+1],nums[j]=nums[j],nums[i+1]
                    break
                j+=1
            i+=1
        return len(set(nums))
        