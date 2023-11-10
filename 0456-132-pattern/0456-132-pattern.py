class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return False
        stack=[nums[-1]]
        com=float('-inf')
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<com:
                return True
            while stack and nums[i]>stack[-1]:
                com=stack.pop()
            stack.append(nums[i])
        return False
                
            