class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=1
        ours=set()
        ours.add(nums[0])
        for j in range (1,len(nums)):
            if nums[j] not in ours:
                nums[i]=nums[j]
                ours.add(nums[j])
                i+=1
        return i
            
            
        