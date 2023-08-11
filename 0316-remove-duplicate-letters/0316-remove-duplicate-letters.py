class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        dic=Counter(s)
        stack=[]
        visited=set()
        for i in range(len(s)):
            if s[i] not in visited:
                while stack and stack[-1] > s[i] and dic[stack[-1]] > 0:
                    visited.remove(stack.pop())
                stack.append(s[i])
            visited.add(s[i])
            dic[s[i]]-=1
        return "".join(stack)