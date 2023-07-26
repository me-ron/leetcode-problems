class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        ans=0
        i=0
        j=0
        while j<len(s):
            if s[i:j+1].count(s[j])>1:
                i+=1
                l-=1
            else:
                l+=1
                j+=1
            ans=max(ans,l)
        return ans
        

        