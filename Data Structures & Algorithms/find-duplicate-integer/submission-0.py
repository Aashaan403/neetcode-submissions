class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        no_duplicate = set()

        for i in range(len(nums)):
            if nums[i] in no_duplicate:
                return nums[i]
            else:
                no_duplicate.add(nums[i])
                

        