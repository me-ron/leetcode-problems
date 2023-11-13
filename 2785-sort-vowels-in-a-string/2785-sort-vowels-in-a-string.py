class Solution:
    def sortVowels(self, s: str) -> str:
        sett={'a','e','i','o','u','A','E','I','O','U'}
        arr=[]
        for i in s:
            if i in sett:
                arr.append(i)
        arr.sort()
        i=0
        new_s=""
        for j in s:
            if j in sett:
                new_s+=arr[i]
                i+=1
            else:
                new_s+=j
                
        return new_s
                
                
        