class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count =defaultdict(lambda :0)
        for n in nums:
            count[n] += 1
        items = sorted(count.items(),key = lambda x:x[1],reverse=True)
        res = []
        for i in range (k):
            res.append(items[i][0])
        

        return res