class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        l,r=0,len(nums)-1
        while k>0:
            nums.insert(0,nums[r])
            nums.pop()
            k-=1