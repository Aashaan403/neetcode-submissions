class Solution:
    def isValid(self, s: str) -> bool:
        openings = ["(","[","{"]
        closings = [")","]","}"]
        stack = []
        for c in s:
            if c in closings:
                if stack and stack[-1] == openings[closings.index(c)]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
                

        
 
        