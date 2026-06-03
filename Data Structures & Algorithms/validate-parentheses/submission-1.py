class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {')':'(','}':'{',']':'['}

        for bracket in s:
            if bracket in brackets.values():
                stack.append(bracket)
            elif stack and stack[-1] == brackets[bracket]:
                stack.pop()
                continue
            else:
                return False
        return False if stack else True