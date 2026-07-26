class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for x in nums:
            count[x] = 1 + count.get(x, 0) 

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        ret =[]
        while len(ret) < k:
            ret.append(arr.pop()[1])
        return ret