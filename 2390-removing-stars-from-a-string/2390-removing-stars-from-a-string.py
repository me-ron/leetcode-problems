class Solution:
    def removeStars(self, s: str) -> str:
        stack =[]
        for i in s:
            if i!='*':
                stack.append(i)
            else:
                if stack is not None:
                    stack.pop()
        return "".join(stack)
            
            