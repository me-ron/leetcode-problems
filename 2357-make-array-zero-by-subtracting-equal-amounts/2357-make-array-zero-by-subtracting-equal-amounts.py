class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans=0
        nums2=set(nums)
        nums2.discard(0)
        return len(nums2)
            
        