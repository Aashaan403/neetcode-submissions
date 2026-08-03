class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        point1 = 0
        point2 =0
        length = 0
        if len(s) ==0:
            return 0
        if len(s) ==1:
            return 1
        while  point2 < len(s):
            if s[point2] not in s[point1:point2]:
                point2+=1
                length = max(length,(point2-point1))
            else:
                index = s[point1:point2].index(s[point2]) + point1
                point1 = index +1
            

        return length


             

        