class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        for i in s:
            temp=""
            if i==")":
                while stack[-1]!="(":
                    temp+=stack.pop()
                stack.pop()
                for j in range(len(temp)):
                    stack.append(temp[j])
            else:
                stack.append(i)
        return("".join(stack))
                    
                
        