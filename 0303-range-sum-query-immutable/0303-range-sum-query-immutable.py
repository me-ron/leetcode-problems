class NumArray:

    def __init__(self, nums: List[int]):
        lst=[0]
        for i in nums:
            lst.append(i+lst[-1])
        self.lst = lst
    def sumRange(self, left: int, right: int) -> int:
        return self.lst[right+1]-self.lst[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)