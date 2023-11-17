class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        def sortt(num):
            return abs(num)
        nums.sort(key=sortt)
        for i in range(len(nums)):
            nums[i]=nums[i]**2
        return nums
        