class Solution:
    def search(self, nums: List[int], target: int) -> int:
        beg = 0
        end = len(nums)-1
        while beg <= end:
            mid = (beg+end)//2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                beg = (beg+end)//2 + 1
            else:
                end = (beg+end)//2 - 1
        
        return -1


        