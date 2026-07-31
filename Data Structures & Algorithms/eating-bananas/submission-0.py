class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minimum = 1
        maximum = max(piles)
        while minimum <= maximum:
            mid = (minimum + maximum) //2
            totaltime = 0
            for p in piles:
                totaltime += math.ceil(float(p)/mid)
            if totaltime <= h:
                    res = mid
                    maximum = mid-1
            else:
                    minimum = mid +1
        return res




                




        




























