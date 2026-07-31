class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for i in range(len(nums))]
        
        prefix,postfix = 1,1

        for i in range(0,len(nums)): # for prefix
            res[i] = prefix
            prefix = nums[i]*prefix
            

        for i in range(len(nums)-1,-1,-1): #for postfix
            res[i] *= postfix
            postfix *= nums[i]
        return res

        
        
            
        