class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        for i in s:
            temp=[]
            if i==")":
                while stack[-1]!="(":
                    temp.append(stack.pop())
                stack.pop()
                stack=stack+temp  
            else:
                stack.append(i)
        return("".join(stack))
                    
                
        