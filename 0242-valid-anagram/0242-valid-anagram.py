class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        st=sorted(list(s))
        tt=sorted(list(t))
        return st==tt
        