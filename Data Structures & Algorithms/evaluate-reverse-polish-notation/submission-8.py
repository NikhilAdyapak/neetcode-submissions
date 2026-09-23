class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        arr = []
        ops = {'+', '-', '*', '/'}
        for t in tokens:
            if t in ops:
                b = arr.pop()
                a = arr.pop()
                if t == '+':
                    arr.append(a + b)
                elif t == '-':
                    arr.append(a - b)
                elif t == '*':
                    arr.append(a * b)
                else:
                    arr.append(int(a / b))
            else:
                arr.append(int(t))
        return arr[0]