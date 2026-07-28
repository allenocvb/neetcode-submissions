class Solution:
    def isValid(self, s: str) -> bool:
        paren = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        stack = []
        for character in s:
            if character in paren:
                if stack and stack[-1] == paren[character]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(character)
        
        return not stack

        


            