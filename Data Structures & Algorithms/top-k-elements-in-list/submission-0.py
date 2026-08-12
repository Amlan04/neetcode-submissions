class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        freq = [[] for i in range(len(nums)+1)]
        for n in nums:
            hashmap[n] = 1+hashmap.get(n,0)
        for n, c in hashmap.items():
            freq[c].append(n)
        size = len(nums)
        res = []
        while k != 0:
            k = k-len(freq[size])
            res.extend(freq[size])
            size -= 1
        return res