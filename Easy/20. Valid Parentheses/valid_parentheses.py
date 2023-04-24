class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses_pairs = {
            "{" : "}",
            "}" : "{",
            "(" : ")",
            ")" : "(",
            "[" : "]",
            "]" : "["
        }
        closed_parenthesis = {")", "}", "]"}
        for parenthesis in s:
            if parenthesis in closed_parenthesis and len(stack) == 0:
                return False
            if parenthesis in closed_parenthesis:
                if parentheses_pairs[parenthesis] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(parenthesis)
        
        if len(stack) > 0:
            return False
        else:
            return True
        
