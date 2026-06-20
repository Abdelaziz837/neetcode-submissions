class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []

        for c in tokens:
            if c == "+":
                secondnum = stack.pop()
                firstnum = stack.pop()
                res = firstnum + secondnum
                stack.append(res)

            elif c == "-":
                secondnum = stack.pop()
                firstnum = stack.pop()
                res = firstnum - secondnum
                stack.append(res)

            elif c == "*":
                secondnum = stack.pop()
                firstnum = stack.pop()
                res = firstnum * secondnum
                stack.append(res)
            elif c == "/":
                secondnum = stack.pop()
                firstnum = stack.pop()
                res = int(firstnum / secondnum)
                stack.append(res)

            else:
                stack.append(int(c))

        return stack.pop()
