class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count=defaultdict(list)
        for i in strs:
            sorted_i=''.join(sorted(i))
            count[sorted_i]+=[i]
        return count.values()
    
            
        