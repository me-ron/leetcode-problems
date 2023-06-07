class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans=0
        while sum(nums)>0:
            nums2=set(nums)
            nums2.discard(0)
            nums2=sorted(list(nums2))
            print(nums2)
            nums=[x-nums2[0] if x!=0 else 0 for x in nums]
            print(nums)
            ans+=1
        return ans
            
        