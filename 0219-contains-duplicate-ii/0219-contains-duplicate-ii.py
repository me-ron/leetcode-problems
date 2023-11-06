class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        se = set()
        i=0
        for j in range (len(nums)):
            if j - i > k:
                se.remove(nums[i])
                i += 1
            if nums[j] in se:
                return True
            se.add(nums[j])
        return False
        