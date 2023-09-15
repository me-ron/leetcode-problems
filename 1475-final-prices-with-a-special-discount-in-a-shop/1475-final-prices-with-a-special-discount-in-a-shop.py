class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans=[]
        for i in range (len(prices)):
            e=prices[i]
            for j in range(i+1,len(prices)):
                if prices[j]<=prices[i]:
                    e-=prices[j]
                    break
            ans.append(e)
        return ans
        