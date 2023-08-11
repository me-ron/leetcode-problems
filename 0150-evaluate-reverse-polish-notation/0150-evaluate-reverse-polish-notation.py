class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            '+': (lambda x, y: operator.add(x, y)),
            '*': (lambda x, y: operator.mul(x, y)),
            '/': (lambda x, y: int(x / y)),
            '-': (lambda x, y: operator.sub(x, y)),
        }
        stack=[]
        for i in tokens:
            if i in operators:
                y=int(stack.pop())
                x=int(stack.pop())
                stack.append(operators[i](x,y))
            else:
                stack.append(i)
        return int(stack[0])
        