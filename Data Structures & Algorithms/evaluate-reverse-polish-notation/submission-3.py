class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t in {"+", "-", "*", "/"}:
                b = stack.pop()
                a = stack.pop()

                if t == "+":
                    res = a + b
                elif t == "-":
                    res = a - b
                elif t == "*":
                    res = a * b
                else:
                    res = a / b

                stack.append(int(res))
            else:
                stack.append(int(t))
            
        return stack[0]