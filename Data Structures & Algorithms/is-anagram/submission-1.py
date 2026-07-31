class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1=len(s)
        l2=len(t)
        if l1 != l2 :
            return False
        return sorted(s) == sorted(t)
            
            


        