class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums2=set(nums)
        return len(nums2)!= len(nums)