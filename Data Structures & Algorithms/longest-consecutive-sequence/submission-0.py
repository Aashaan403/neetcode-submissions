class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set1 = set(nums)
        ans =0
        for i in set1 :
            count = 0
            if i-1 not in set1:
                while i+count in set1:
                    count = count +1
            if count>ans:
                ans= count
        return ans
       
        