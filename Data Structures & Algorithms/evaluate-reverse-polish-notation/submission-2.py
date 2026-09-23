class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {"+", "-", "*", "/"}
        for t in tokens:
            if t in ops:
                b = stack.pop()
                a = stack.pop()
                if t == "+": stack.append(a + b)
                elif t == "-": stack.append(a - b)
                elif t == "*": stack.append(a * b)
                else: stack.append(int(a / b))   # truncate toward zero
            else:
                stack.append(int(t))
        return stack[0]