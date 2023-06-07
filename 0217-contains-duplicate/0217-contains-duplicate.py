from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic=Counter(nums)
        ans=[]
        for i in dic:
            if dic[i]==1:
                ans.append(0)
            else:
                ans.append(1)
        if sum(ans)==0:
            return False
        else:
            return True