class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i in range(len(numbers)-1):
            p1=i
            for j in range(p1+1,len(numbers)):
                p2 = j
                if numbers[p1]+numbers[p2] == target:
                    
                    return [p1+1,p2+1]
        
        