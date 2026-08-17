class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        search = set()
        for n in nums:
            search.add(n)
        max_len = 0
        for n in nums:
            current_len = 0
            if (n-1) not in search:
                current_len += 1
                while (n+current_len) in search:
                    current_len += 1
                max_len = max(current_len,max_len)
        return max_len

        
        