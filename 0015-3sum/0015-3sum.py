class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        for i in range (len(nums)):
            x=nums[i]*-1
            j=i+1
            k=len(nums)-1
            while j<k:
                if nums[j]+nums[k]==x and [nums[i],nums[j],nums[k]] not in ans:
                    ans.append([nums[i],nums[j],nums[k]])
                elif nums[j]+nums[k]>x:
                    k-=1
                else:
                    j+=1
        return ans
        